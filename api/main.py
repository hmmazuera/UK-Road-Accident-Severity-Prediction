from fastapi import FastAPI
from api.schemas import CollisionInput, PredictionOutput
from api.prediction import predict_collision_severity

app = FastAPI(
    title = "UK Road Accident Severity Prediction API",
    description = "This API predicts the severity of road accidents in the UK based on various input features.",
    version = "1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "The API is running and healthy."}

@app.get("/")
def root():
    return {"message": "Welcome to the UK Road Accident Severity Prediction API!"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: CollisionInput):
    input_data = data.model_dump()
    prediction = predict_collision_severity(input_data)
    return prediction

