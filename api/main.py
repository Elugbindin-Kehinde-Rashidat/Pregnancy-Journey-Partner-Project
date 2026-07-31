from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from pathlib import Path


# --------------------------------------------------
# 1. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Maternal Health Risk Prediction API",
    description="API for predicting maternal health risk levels",
    version="1.0.0"
)


# --------------------------------------------------
# 2. Locate and load the trained model
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 3. Define input data
# --------------------------------------------------

class MaternalHealthData(BaseModel):

    age_years: float
    gravidity: float
    parity: float
    gestational_age_weeks: float
    bmi_pre_pregnancy: float
    systolic_bp_mmhg: float
    diastolic_bp_mmhg: float
    hemoglobin_gdl: float
    fasting_glucose_mgdl: float
    proteinuria: float
    hiv_status: int
    anc_visits: float
    delivery_mode: int
    pregnancy_outcome: int


# --------------------------------------------------
# 4. Risk-level mapping
# --------------------------------------------------

risk_mapping = {
    0: "High Risk",
    1: "Low Risk",
    2: "Mid Risk"
}


# --------------------------------------------------
# 5. Home endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Maternal Health Risk Prediction API is running"
    }


# --------------------------------------------------
# 6. Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(data: MaternalHealthData):

    # Arrange features in the EXACT same order
    # used during model training

    input_data = np.array([[
        data.age_years,
        data.gravidity,
        data.parity,
        data.gestational_age_weeks,
        data.bmi_pre_pregnancy,
        data.systolic_bp_mmhg,
        data.diastolic_bp_mmhg,
        data.hemoglobin_gdl,
        data.fasting_glucose_mgdl,
        data.proteinuria,
        data.hiv_status,
        data.anc_visits,
        data.delivery_mode,
        data.pregnancy_outcome
    ]])


    # Make prediction
    prediction = model.predict(input_data)

    predicted_class = int(prediction[0])

    predicted_risk = risk_mapping[predicted_class]


    # Get prediction probabilities
    probabilities = model.predict_proba(input_data)[0]


    return {
        "predicted_class": predicted_class,
        "predicted_risk": predicted_risk,
        "probabilities": {
            "High Risk": round(float(probabilities[0]), 4),
            "Low Risk": round(float(probabilities[1]), 4),
            "Mid Risk": round(float(probabilities[2]), 4)
        }
    }