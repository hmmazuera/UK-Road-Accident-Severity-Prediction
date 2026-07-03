# UK-Road-Accident-Severity-Prediction
End-to-end Machine Learning project using official UK Department for Transport road collision data to predict accident severity.

## Project Overview

This project predicts the severity of road traffic collisions in the UK using official STATS19 road safety data from the Department for Transport.

The project covers the full machine learning workflow:

- Data cleaning
- Data integration
- Exploratory data analysis
- Feature engineering
- Model training and evaluation
- FastAPI backend
- Streamlit web application

## Problem Statement

Road traffic collisions can have different severity levels depending on road, environmental, vehicle and casualty-related factors.

The objective of this project is to build a machine learning model capable of predicting whether a collision is likely to be:

- Fatal
- Serious
- Slight

## Dataset

Source: UK Department for Transport Road Safety Open Data.

The project uses three official datasets:

- Collision data
- Vehicle data
- Casualty data

Only records from 2010 onwards were used to keep the dataset more representative of modern road conditions.

## Machine Learning Approach

Several classification models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost

The final model selected was a Random Forest classifier.

## Final Model Performance

| Metric | Score |
|--------|------:|
| Accuracy | 0.7858 |
| Precision Macro | 0.4730 |
| Recall Macro | 0.4418 |
| F1 Macro | 0.4538 |

F1 Macro was used as the main metric because the dataset is highly imbalanced.

## Application

The project includes:

- A FastAPI backend for model inference
- A Streamlit web app for user interaction
- Prediction probabilities for each severity class
- Interactive map based on collision location

## How to Run Locally

Install dependencies:
pip install -r requirements.txt

Run FastAPI:
uvicorn api.main:app

Run Streamlit app:
streamlit run app/streamlit_app.py

FastAPI documentation:
http://127.0.0.1:8000/docs

## Author

Mauricio Mazuera
- LinkedIn: "https://www.linkedin.com/in/mauricio-mazuera-a0a7a933b/"
- GitHub: "https://github.com/hmmazuera/UK-Road-Accident-Severity-Prediction"