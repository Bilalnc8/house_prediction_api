from fastapi import FASTAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version

app = FASTAPI()

app.get("/")

class Inputs(BaseModel):
    asking_price: int
    bedrooms: int
    bathrooms: int
    parking: int
    typeOf: int
    sqft: int
    
class PredictionOut(BaseModel):
    Prediction: int

def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: Inputs):
    prediction = predict_pipeline(payload.text)
    return {"Prediction": prediction}