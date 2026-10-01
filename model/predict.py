import pickle
import pandas as pd


# ============================================================
# Load ML Model
# ============================================================

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


# ============================================================
# Model Version
# ============================================================

model_version = "1.0.0"


# ============================================================
# Prediction Function
# ============================================================

def predict_output(user_input: dict):
    """
    Generate prediction and probability for each premium category.
    """

    # Convert input dictionary into DataFrame
    input_df = pd.DataFrame([user_input])

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = model.predict(input_df)[0]

    # --------------------------------------------------------
    # Prediction Probability
    # --------------------------------------------------------

    probabilities = model.predict_proba(input_df)[0]

    # Get class names from the trained model
    classes = model.classes_

    confidence = {
        str(class_name): round(float(probability) * 100, 2)
        for class_name, probability in zip(classes, probabilities)
    }

    return {
        "prediction": str(prediction),
        "confidence": confidence
    }
