from __future__ import print_function

import argparse
import os
from xml.sax import default_parser_list
import pandas as pd
from sklearn import tree

import joblib


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Sagemaker specific arguments. Defaults are set in the environment variables.

    #Saves Checkpoints and graphs
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])

    #Save model artifacts
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])

    #Train data
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    file = os.path.join(args.train, "water_potability.csv")
    dataset = pd.read_csv(file, engine="python")
    dataset['Potability'] = dataset['Potability'].astype('float64')
    dataset.dropna(inplace=True)

    X = dataset[['ph','Solids','Turbidity']]
    y = dataset['Potability']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

    from sklearn.linear_model import LogisticRegression
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)

    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(regressor, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    """Deserialized and return fitted model
    
    Note that this should have the same name as the serialized model in the main method
    """
    regressor = joblib.load(os.path.join(model_dir, "model.joblib"))
    return regressor