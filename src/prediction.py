import joblib
import numpy as np
from pathlib import Path


# ============================================
# Load trained Random Forest model
# ============================================

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "random_forest.pkl"
)

model = joblib.load(MODEL_PATH)


# ============================================
# Risk category mapping
# ============================================

RISK_MAPPING = {
    0: "High Risk",
    1: "Low Risk",
    2: "Mid Risk"
}


# ============================================
# Pregnancy Risk Prediction
# ============================================

def predict_pregnancy_risk(
    age_years,
    gravidity,
    parity,
    gestational_age_weeks,
    bmi_pre_pregnancy,
    systolic_bp_mmhg,
    diastolic_bp_mmhg,
    hemoglobin_gdl,
    fasting_glucose_mgdl,
    proteinuria,
    hiv_status,
    anc_visits,
    delivery_mode,
    pregnancy_outcome
):

    input_data = np.array([[
        age_years,
        gravidity,
        parity,
        gestational_age_weeks,
        bmi_pre_pregnancy,
        systolic_bp_mmhg,
        diastolic_bp_mmhg,
        hemoglobin_gdl,
        fasting_glucose_mgdl,
        proteinuria,
        hiv_status,
        anc_visits,
        delivery_mode,
        pregnancy_outcome
    ]])

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    risk_level = RISK_MAPPING[int(prediction)]

    return {
        "risk_level": risk_level,
        "prediction_class": int(prediction),
        "probabilities": probabilities.tolist()
    }