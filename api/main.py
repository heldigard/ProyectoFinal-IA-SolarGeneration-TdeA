from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from model import predict_lgbm, SolarGenerationData

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Solar Generation Prediction API"}

@app.post("/predict")
def predict(data: SolarGenerationData):
    # Convertir los datos de entrada a un DataFrame de pandas
    input_data = pd.DataFrame([data.dict()])
    # Obtener la predicción
    prediction = predict_lgbm(input_data)
    # Devolver la predicción
    return prediction
