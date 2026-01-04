import joblib
# import pandas as pd
# import numpy as np
from fastapi import FastAPI
from schema import Input_Features
app=FastAPI()


model=joblib.load("model.joblib")


@app.get("/")
def Home_page():
    return {"Messages":'Welcome to Homepage for Model Predicition'}

@app.post("/predict")
def model_predicition(features:Input_Features):
    data=features.to_list()
    y_pred=model.predict([data])
    return {"Prediction":f"Flower is {y_pred[0]}"}
