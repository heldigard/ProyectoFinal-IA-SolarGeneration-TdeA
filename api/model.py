import joblib
import pandas as pd
from pydantic import BaseModel

# Cargar el modelo de LightGBM
lgbm_model = joblib.load("best_model_pipeline.pkl")


def predict_lgbm(data: pd.DataFrame):
    prediction = lgbm_model.predict(data)
    return {
        "AC Power in Watts": int(prediction[0]),
    }


class SolarGenerationData(BaseModel):
    MODULE_TEMP: float
    Amb_Temp: float
    IRR: float
