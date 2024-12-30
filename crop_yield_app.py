import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from catboost import CatBoostRegressor

# Title of the App
st.title("FarmBot.ai")
st.write("""
### Predict crop yield based on input features!
""")

# Load Local Dataset
DATA_PATH = "./train.csv"  # Update this path with the location of your CSV file
try:
    df = pd.read_csv(DATA_PATH)
   

    # Verify Required Columns
    if 'Crop_Yield (kg/ha)' not in df.columns:
        st.error("The dataset must contain the 'Crop_Yield (kg/ha)' column.")
    else:
        # Prepare Features and Target
        X_train = df.drop(columns=['Crop_Yield (kg/ha)', 'id'])  # Drop target and ID column
        y_train = df['Crop_Yield (kg/ha)']
        categorical_features = ['State', 'Crop_Type', 'Soil_Type']

        # Train-Test Split
        

        # Train CatBoost Model
        model = CatBoostRegressor(
            iterations=100, depth=6, learning_rate=0.1, loss_function='RMSE', random_seed=42, verbose=0
        )
        model.fit(X_train, y_train, cat_features=categorical_features)

        # Sidebar Inputs
        st.sidebar.header("Input Features")
        year = st.sidebar.number_input("Year", min_value=1800, max_value=2100, step=1, value=2025)
        state = st.sidebar.selectbox("State", df['State'].unique())
        crop_type = st.sidebar.selectbox("Crop Type", df['Crop_Type'].unique())
        rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, step=0.1, value=500.0)
        soil_type = st.sidebar.selectbox("Soil Type", df['Soil_Type'].unique())
        irrigation_area = st.sidebar.number_input("Irrigation Area (ha)", min_value=0.0, step=1.0, value=500.0)

        # Prepare Input Data for Prediction
        input_data = pd.DataFrame({
            'Year': [year],
            'State': [state],
            'Crop_Type': [crop_type],
            'Rainfall': [rainfall],
            'Soil_Type': [soil_type],
            'Irrigation_Area': [irrigation_area]
        })

        # Make Prediction
        if st.sidebar.button("Predict Crop Yield"):
            prediction = model.predict(input_data)
            st.write(f"### Predicted Crop Yield: **{prediction[0]:.2f} kg/ha**")

       
except FileNotFoundError:
    st.error(f"File not found: {DATA_PATH}. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")

