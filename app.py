import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

ages = np.array([5, 8, 10, 12, 15, 18]).reshape(-1, 1)
heights = np.array([110, 128, 138, 150, 168, 175])
weights = np.array([18, 26, 32, 42, 58, 70])

height_model = LinearRegression().fit(ages, heights)
weight_model = LinearRegression().fit(ages, weights)

st.title("Age to Height & Weight Predictor")

age = st.slider("Age", 5, 18, 10)

if st.button("Predict"):
    pred_height = height_model.predict([[age]])[0]
    pred_weight = weight_model.predict([[age]])[0]
    st.success(f"Estimated Height: {pred_height:.1f} cm")
    st.success(f"Estimated Weight: {pred_weight:.1f} kg")
