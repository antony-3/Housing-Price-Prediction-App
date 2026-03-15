from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import numpy as np


model = joblib.load("/Users/user/Documents/housing_project/backend/model.pkl")
scaler_X = joblib.load("/Users/user/Documents/housing_project/backend/scaler_X.pkl")
scaler_y = joblib.load("/Users/user/Documents/housing_project/backend/scaler_y.pkl")
app = FastAPI()

class HousingData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population:float
    household: float
    median_income: float

@app.get("/")
def get_health():
    return{"status": "running"}

@app.get("/info")
def get_info():
    return{"Housing model prediction API"}

@app.post("/predict")
async def get_prediction(data:HousingData):
    input_data = np.array([[data.longitude, data.latitude, data.housing_median_age, data.total_rooms, 
                           data.total_bedrooms, data.population, data.household, data.median_income]])
    input_scaled = scaler_X.transform(input_data)

    pred_scaled = model.predict(input_data)[0]

    prediction = scaler_y.inverse_transform(pred_scaled.reshape(-1, 1))[0, 0]

    return{'prediction': float(prediction)}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
