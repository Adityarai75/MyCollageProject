import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))



@flask_app.route("/")
def Home():
    return render_template("RAINFALL_PRIDICTION.HTML")

@flask_app.route("/rainfall")
def rainfall():
    return render_template("rainfall.html")

@flask_app.route("/About")
def About():
    return render_template("About.html")

@flask_app.route("/Weather_Forecasting")
def Weather_Forecasting():
    return render_template("Weather_Forecasting.html")

@flask_app.route("/Topics")
def Topics():
    return render_template("Topics.html")

@flask_app.route("/Source")
def Source():
    return render_template("Source.html")


    


@flask_app.route("/predict",methods=["POST"])
def predict():
    year = float(request.form['year'])
    state = request.form['state'] 
    features = [[state, year]] 
    prediction = model.predict(features)
    #output = round(prediction[0], 2) 
    return render_template("RAINFALL_PRIDICTION.HTML",prediction_text="the average of rainfall is :>===>> {}".format(prediction))
    return render_template("RAINFALL_PREDICTION.html", states=state)

if __name__ == "__main__":
    flask_app.run(debug=True)
    
