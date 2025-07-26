# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---- SETTINGS ----
FEATURES = [
    'urb_pop_growth_perc',
    'gni_per_cap',
    'cereal_yield',
    'pop_growth_perc',
    'en_per_cap',
    'pop_urb_aggl_perc',
    'prot_area_perc'
]

# ---- LOAD MODEL & DATA ----
@st.cache_resource
def load_model():
    return joblib.load("forecasting_co2_emmision.pkl")  # Save this using joblib.dump(model, 'rf_model.pkl')

@st.cache_data
def load_data():
    return pd.read_csv("data_cleaned.csv")

model = load_model()
data = load_data()

# ---- STREAMLIT UI ----
st.title("CO₂ Per Capita Predictor")
st.write("Adjust future values for selected features to forecast CO₂ emissions.")

# Country selector
country = st.sidebar.selectbox("Select a Country", sorted(data['country'].unique()))
country_data = data[data['country'] == country].sort_values("year")

# Display latest available values
st.subheader(f"Latest Data for {country}")
latest = country_data.dropna(subset=FEATURES).iloc[-1]
st.write(latest[['year'] + FEATURES])

# Input form for new values
st.subheader("Adjust Feature Values")
input_data = []

with st.form("prediction_form"):
    for feature in FEATURES:
        val = st.number_input(
            label=f"{feature}",
            value=float(latest[feature]),
            step=0.1
        )
        input_data.append(val)

    submitted = st.form_submit_button("Predict CO₂ per Capita")

# ---- PREDICTION ----
if submitted:
    X_input = np.array(input_data).reshape(1, -1)
    prediction = model.predict(X_input)[0]
    st.success(f"Predicted CO₂ per Capita: {prediction:.3f}")

# ---- Footer ----
st.markdown("""
---
App powered by Random Forest Regressor. Built with Streamlit.
""")
