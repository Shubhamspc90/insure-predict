from pydantic import BaseModel


# ============================================================
# Confidence Schema
# ============================================================

class PredictionConfidence(BaseModel):

    Low: float
    Medium: float
    High: float


# ============================================================
# Prediction Features Schema
# ============================================================

class PredictionFeatures(BaseModel):

    bmi: float
    age_group: str
    lifestyle_risk: str
    city_tier: int


# ============================================================
# Prediction Response Schema
# ============================================================

class PredictionResponse(BaseModel):

    success: bool
    predicted_category: str
    confidence: PredictionConfidence
    features: PredictionFeatures
