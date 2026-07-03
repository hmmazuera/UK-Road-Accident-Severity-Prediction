from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

PREPROCESSOR_PATH = BASE_DIR / "models" / "production_preprocessor.joblib"
MODEL_PATH = BASE_DIR / "models" / "production_model.joblib"

SEVERITY_LABELS = {
    1: "Fatal",
    2: "Serious",
    3: "Slight",
}


preprocessor = joblib.load(PREPROCESSOR_PATH)
model = joblib.load(MODEL_PATH)


def predict_collision_severity(input_data: dict) -> dict:
    input_df = pd.DataFrame([input_data])

    expected_columns = list(preprocessor.feature_names_in_)
    input_df = input_df[expected_columns]

    processed_input = preprocessor.transform(input_df)

    prediction = int(model.predict(processed_input)[0])

    result = {
        "prediction_code": prediction,
        "prediction_label": SEVERITY_LABELS.get(prediction, "Unknown"),
    }

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(processed_input)[0]

        result["probabilities"] = {
            SEVERITY_LABELS.get(int(class_label), str(class_label)): float(prob)
            for class_label, prob in zip(model.classes_, probabilities)
        }

    return result