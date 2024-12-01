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
    input_data = pd.DataFrame([data.dict(by_alias=True)])
    input_data.rename(columns={"IRR_W_m2": "IRR (W/m2)"}, inplace=True)  # Renombrar la columna
    # Obtener la predicción
    prediction = predict_lgbm(input_data)
    # Devolver la predicción
    return prediction