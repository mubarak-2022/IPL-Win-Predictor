# IPL Win Predictor

This repository contains a project that predicts the outcomes of IPL cricket matches using machine learning, specifically Logistic Regression. The project aims to provide real-time win predictions based on live match data. Built using **Python**, the project leverages **Streamlit** for the web interface and is deployed on **Render** for public access.

## Key Features
- **Live Match Data Inputs**: The model uses essential match information like batting and bowling teams, city, runs left, wickets left, balls left, and both current and required run rates to predict the outcome of the match.
- **Logistic Regression Model**: The final classification model is built using **Logistic Regression**. This model is chosen for its simplicity and effectiveness in handling binary classification problems. The win probability is generated using the `predict_proba` method, which provides the probability for both losing and winning outcomes.
- **Interactive Web Interface**: Users can input live match data through a user-friendly web app built with **Streamlit**. The app then predicts the probability of winning or losing based on the provided inputs.
- **Real-Time Predictions**: The predictions are displayed in real time, providing insights during a live match scenario.

## Dataset
The dataset used includes ball-by-ball match data:
- **Batting Team**
- **Bowling Team**
- **City** (location of the match)
- **Runs Left**
- **Balls Left**
- **Wickets Left**
- **Total Runs** (Target)
- **Current Run Rate (CRR)**
- **Required Run Rate (RRR)**

## Model and Prediction
- **Logistic Regression**: The final model chosen for this project is a Logistic Regression classifier. It is designed to predict the probability of a win or a loss. The output is a probability score for each class: 0 (Loss) and 1 (Win). The `predict_proba` function is used to generate these probabilities, allowing users to see how confident the model is in its prediction.
- **Machine Learning Pipeline**: A pipeline with column transformers is used to preprocess categorical and numerical features before feeding them into the Logistic Regression model.

## Web Application
- **Frontend**: The web application is developed using **Streamlit**, which provides an interactive interface for users to enter match details.
- **Deployment**: The app is deployed on **Render**, allowing easy access for users to input match data and receive predictions.

