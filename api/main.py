from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from model import predict_lgbm, SolarGenerationData

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    MODULE_TEMP: float = Form(...),
    Amb_Temp: float = Form(...),
    IRR_W_m2: float = Form(...),
):
    data = SolarGenerationData(
        MODULE_TEMP=MODULE_TEMP, Amb_Temp=Amb_Temp, IRR_W_m2=IRR_W_m2
    )
    input_data = pd.DataFrame([data.dict(by_alias=True)])
    input_data.rename(columns={"IRR_W_m2": "IRR (W/m2)"}, inplace=True)
    prediction = predict_lgbm(input_data)

    return templates.TemplateResponse(
        "form.html", {"request": request, "prediction": prediction}
    )
