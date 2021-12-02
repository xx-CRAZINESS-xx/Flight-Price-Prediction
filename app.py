from flask import Flask, request, render_template
import numpy as np
import pickle
import pandas as pd
import datetime
from utils import day_part
import category_encoders 
import shap
from  lightgbm import LGBMRegressor


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
encoder=pickle.load(open('encoder.pkl','rb'))


@app.route("/")

def home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])

def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Date = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

        Weekday=str(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").strftime("%A"))

        # Departure
        Dep_Hour = str(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_Min = str(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_Hour = str(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_Min = str(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        # Duration
        hour=datetime.datetime.strptime(Arrival_Hour,"%H")-datetime.datetime.strptime(Dep_Hour,"%H")
        Duration_Hours=hour.total_seconds()/3600
        Duration_Hours=np.abs(Duration_Hours)

        Duration_Mins=datetime.datetime.strptime(Arrival_Min,"%M")-datetime.datetime.strptime(Dep_Min,"%M")
        Duration_Mins=Duration_Mins.total_seconds()/60



        # Total Stops
        Total_Stops = int(request.form["stops"])
        Airline=request.form['airline']
    
        # Source
        Source = request.form["Source"]

        # Destination
        Destination=request.form['Destination']

        data=[[Airline, Source, Destination, Total_Stops, Dep_Hour,
                Dep_Min, Arrival_Hour, Arrival_Min, Date, Month,
                Duration_Hours, Duration_Mins, Weekday]]

        df=pd.DataFrame(data,columns=['Airline', 'Source', 'Destination', 'Total_Stops', 'Dep_Hour',
       'Dep_Min', 'Arrival_Hour', 'Arrival_Min', 'Date', 'Month',
       'Duration_Hours', 'Duration_Mins', 'Weekday'])

        df['Dep_Hour']=df['Dep_Hour'].astype('int64')
        df['Dep_Min']=df['Dep_Min'].astype('int64')
        df['Arrival_Hour']=df['Arrival_Hour'].astype('int64')
        df['Arrival_Min']=df['Arrival_Min'].astype('int64')



        df['Weekday'] = df['Weekday'].map({'Monday': 1,'Tuesday': 2,'Wednesday': 3,'Thursday': 4,'Friday': 5,'Saturday': 6,'Sunday': 7})

        df['day/night'] = df['Dep_Hour'].apply(day_part)

        df['day/night'] = df['day/night'].map({'Early Morning': 1,'Morning': 2,'Noon/Afternoon': 3,'Evening': 4,'Night': 5,'Late Night': 6})

        df['day/night']=df['day/night'].fillna(6)

        X=encoder.transform(df)

        output=model.predict(X)
        output=np.round(output[0])
        return render_template('home.html',prediction_text="YOUR FLIGHT PRICE IS ₹ {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
