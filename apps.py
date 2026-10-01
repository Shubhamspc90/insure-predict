from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.user_input import UserInput
from schema.response import PredictionResponse

from model.predict import (
    predict_output,
    model_version,
    model
)


# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(
    title="Insurance Premium Category API",
    description="API for predicting insurance premium category",
    version="1.0.0"
)


# ============================================================
# Root Endpoint
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Insurance Premium Category API is running",
        "docs": "/docs"
    }


# ============================================================
# Health Check Endpoint
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "version": model_version,
        "model_loaded": model is not None
    }


# ============================================================
# Prediction Endpoint
# ============================================================

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_premium(data: UserInput):

    # --------------------------------------------------------
    # Prepare input for ML model
    # --------------------------------------------------------

    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    try:

        result = predict_output(user_input)

        prediction = result["prediction"]
        confidence = result["confidence"]

        # ----------------------------------------------------
        # Successful Response
        # ----------------------------------------------------

        return {
            "success": True,
            "predicted_category": prediction,
            "confidence": confidence,
            "features": {
                "bmi": data.bmi,
                "age_group": data.age_group,
                "lifestyle_risk": data.lifestyle_risk,
                "city_tier": data.city_tier
            }
        }

    # --------------------------------------------------------
    # Error Handling
    # --------------------------------------------------------

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Prediction failed",
                "error": str(e)
            }
        )
