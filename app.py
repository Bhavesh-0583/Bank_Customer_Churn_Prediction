import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl","rb"))

st.title("🏦 Bank Customer Churn Prediction App")

st.write("Predict whether a customer will leave the bank.")

# User Inputs
credit_score = st.number_input("Credit Score", 300, 900)
age = st.slider("Age",18,100)
tenure = st.slider("Tenure",0,10)

balance = st.number_input("Balance")
num_products = st.slider("Number of Products",1,4)

has_credit_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])

estimated_salary = st.number_input("Estimated Salary")

# Input dataframe
input_data = pd.DataFrame({
    "CreditScore":[credit_score],
    "Age":[age],
    "Tenure":[tenure],
    "Balance":[balance],
    "NumOfProducts":[num_products],
    "HasCrCard":[has_credit_card],
    "IsActiveMember":[is_active_member],
    "EstimatedSalary":[estimated_salary]
})

# Scale
prediction = model.predict(input_data)

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Customer will leave the bank")
    else:
        st.success("✅ Customer will stay")
