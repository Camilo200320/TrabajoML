import pickle
import pandas as pd


with open("models/RFDcultivo.pkl", "rb") as file:
    RFDc = pickle.load(file)

with open("models/svm_model.pkl", "rb") as file:
    svm_model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


columns = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

def predictRF(data):
    df = pd.DataFrame([data], columns=columns)
    return RFDc.predict(df)[0]

def predictSVM(data):
    df = pd.DataFrame([data], columns=columns)
    data_scaled = scaler.transform(df)
    return svm_model.predict(data_scaled)[0]