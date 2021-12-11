
# Project Title

### Flight Price Prediction

Travelling through flights has become an integral part of today's lifestyle as more and more are opting for fster travelling oprions. The flight ticket prices increase or decrease every now and then depending on various factors such as timings of the flight, destination, duration, festive seasons etc. Therefore having  some basic idea of the flight fares before planning the trip will surely help many people save money and time.

The main goal is to predict the price of the flights based on different factors available in the dataset.

## Screenshot

![Alt text](https://github.com/xx-CRAZINESS-xx/Flight-Price-Prediction/blob/main/static/image/Screenshot.png?raw=true)


## Heroku Link

https://flight---price---prediction.herokuapp.com/

## Dataset Link

https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh
## Installation

 * Create a new environment

 * Copy the downloaded files or clone the files from github to your environment 

 * pip3 install -r requirements.txt

 * python app.py
## EDA

* Seperated hour, minutes, day and month from date and time related columns

* Crated a new column which shows the day part like morning, noon etc

* Removed outliers using IQR 

* Replaced hours that were greater than 24 like {25:1,26:2,27:3} etc

## Model creation 

* Encoded categorical variables using category encoders

* Used Linear Regression and Lasso as a baseline model which gave and r2 of 62.71% and RMSE of 2582

* Used RandomForest Regressor and LightGBM Regressor for increasing the performance

* Used optuna for tuning RandomForest and LightGBM 

* Chose LightGBM Regressor as the best model with test r2 of 86.74%, MAE of 1097.25 and RMSE of 1539.56


## Model Explainability

* Used Shap for Model Explainability

![Alt text](https://github.com/xx-CRAZINESS-xx/Flight-Price-Prediction/blob/main/static/image/shap.png?raw=true)

## Future Improvements
* UI

* If you set the arrival date and time which is less than the departure date and time, the model still gives an output which should be improved
