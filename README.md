# FarmBot.ai - Crop Yield Prediction

Welcome to **FarmBot.ai** – an AI-powered web application designed to predict crop yields based on various agricultural inputs. This app uses machine learning models to help farmers and agronomists predict the expected crop yield, optimizing farming decisions for better productivity.

## Overview

This app leverages data about weather, soil conditions, irrigation, and other agricultural factors to predict crop yields. The app uses a **CatBoost Regressor** model to make predictions based on the features provided by the user.

### Features:
- **Predict Crop Yield**: Using user inputs such as year, state, crop type, rainfall, soil type, and irrigation area.
- **Data-driven**: The app uses historical crop yield data to train the model and predict future yields.
- **User-friendly**: Simple and interactive interface with easy-to-use sliders, inputs, and dropdowns.

## Live App Link

You can access the live version of the app here:  
[FarmBot.ai - Crop Yield Prediction](https://farmbotai.streamlit.app/)

## Getting Started

To run this app locally or deploy it on Streamlit Cloud, follow these steps:

### Prerequisites

You need to have Python installed along with the following libraries:

- **Streamlit**: To run the web app.
- **Pandas**: To load and manipulate the data.
- **scikit-learn**: For model evaluation functions like `train_test_split` and `mean_squared_error`.
- **CatBoost**: The regression model used for crop yield prediction.

### Installation

1. Clone this repository or download the app files to your local machine.

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required libraries from requirements.txt:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   ```bash
   streamlit run crop_yield_app.py
5. Visit http://localhost:8501 on your browser to view the app.

### Features in the App:
- **Title & Description**: Introduces users to the app with a title and brief description.
- **Dataset Loading**: Loads the train.csv file and checks for the required columns.
- **Sidebar Inputs**: Allows users to input features such as:
    - Year
    - State
    - Crop Type
    - Rainfall
    - Soil Type
    - Irrigation Area
- **Model Training**: Trains a CatBoost Regressor on the provided dataset and uses it to predict crop yield.

