import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('RidgeModel.pkl', 'rb'))

st.title("🏠 Bengaluru House Price Prediction")

location = st.text_input("Location")
sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)

if st.button("Predict Price"):
    location = location.strip() 
    # Create dataframe (IMPORTANT)
    input_df = pd.DataFrame({
        'location': [location],
        'total_sqft': [sqft],
        'bath': [bath],
        'bhk': [bhk]
    })

    prediction = model.predict(input_df)

    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")