# water_prediction

This project tells us about whether the water is drinkable or not. This project consists of both the hardware and the software. We will found out the chemicals in the water using the appropriate sensors and a microcontroller is used. An ML model is used for predicting whether the water is drinkable or not using the sensor data.

For the accurate result of the water potability, we need a total of 10 characteristics of the water, those are mentioned in the dataset(it is in the sagemaker folder), for testing I have taken only one characteristic that is turbidity. Using this value I have predicted whether the water is drinkable or not.


In this project, I have used the [turbidity sensor](https://www.amazon.in/Generic-Turbidity-Sensor-with-Module/dp/B09LQY559W/ref=asc_df_B09LQY559W/?tag=googleshopdes-21&linkCode=df0&hvadid=588048897591&hvpos=&hvnetw=g&hvrand=13799334506488912913&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299297&hvtargid=pla-1650636944282&psc=1), and we should select the microcontroller which is able to connect to internet since we cannot run a ML model on a microcontroller which requires a lot of computing power that will be not available. I have used [NodeMcu](https://www.amazon.in/Easy-Electronics-NodeMcu-Development-Board/dp/B06XYRS6KC). After making connecting, test whether the values are coming from the sensor or not.
