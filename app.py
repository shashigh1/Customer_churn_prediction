import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle

# Load model and preprocessing objects
@st.cache_resource
def load_resources():
    model = tf.keras.models.load_model("model.keras")
    ss = pickle.load(open('ss.pkl', 'rb'))
    le_gender = pickle.load(open('label_encoder.pkl', 'rb'))
    ohe_geo = pickle.load(open('ohe_geo.pkl', 'rb'))
    return model, ss, le_gender, ohe_geo

model, ss, le_gender, ohe_geo = load_resources()

st.title("Customer Churn Prediction")

with st.form("input_form"):
    geography = st.selectbox("Geography", options=list(ohe_geo.categories_[0]))
    gender = st.selectbox("Gender", options=list(le_gender.classes_))
    age = st.number_input("Age", min_value=18, max_value=100)
    credit_score = st.number_input("Credit Score", min_value=0, max_value=1000)
    tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10)
    balance = st.number_input("Balance", min_value=0.0)
    num_of_products = st.number_input("Number of Products", min_value=1, max_value=10, step=1)
    has_cr_card = st.selectbox("Has Credit Card?", options=[0, 1])
    is_active_member = st.selectbox("Is Active Member?", options=[0, 1])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0)

    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare input DataFrame
    df = pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [le_gender.transform([gender])[0]],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary]
    })

    # One-hot encode geography
    geo_encoded = ohe_geo.transform([[geography]]).toarray()
    geo_df = pd.DataFrame(geo_encoded, columns=ohe_geo.get_feature_names_out(['Geography']))
    df = pd.concat([df, geo_df], axis=1)

    # Scale features
    X = ss.transform(df)

    # Predict
    pred_prob = model.predict(X)[0][0]
    churn = pred_prob > 0.5

    st.write(f"**Churn Probability:** {pred_prob:.2f}")
    if churn:
        st.error("⚠ The customer is **likely to churn**.")
    else:
        st.success("✔ The customer is **not likely to churn**.")
