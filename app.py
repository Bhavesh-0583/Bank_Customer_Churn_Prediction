import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🏦 Bank Customer Churn Prediction App")

st.write("Enter customer details to predict whether the customer will leave the bank.")

# -------------------------
# User Inputs
# -------------------------

credit_score = st.number_input("Credit Score", 300, 900, 600)

age = st.slider("Age", 18, 100, 30)

tenure = st.slider("Tenure (Years with bank)", 0, 10, 3)

balance = st.number_input("Account Balance", 0.0, 250000.0, 50000.0)

num_products = st.slider("Number of Bank Products", 1, 4, 1)

has_credit_card = st.selectbox("Has Credit Card", [0,1])

is_active_member = st.selectbox("Is Active Member", [0,1])

estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

geography = st.selectbox("Geography", ["France","Germany","Spain"])

gender = st.selectbox("Gender", ["Male","Female"])

# -------------------------
# Encoding categorical variables
# -------------------------

geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0
gender_male = 1 if gender == "Male" else 0

# -------------------------
# Create DataFrame (same structure as training data)
# -------------------------

input_data = pd.DataFrame({
    'CreditScore':[credit_score],
    'Geography_Germany':[geo_germany],
    'Geography_Spain':[geo_spain],
    'Gender_Male':[gender_male],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_products],
    'HasCrCard':[has_credit_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
})

# -------------------------
# Prediction
# -------------------------

if st.button("Predict"):

    prediction = model.predict(input_data)

    try:
        probability = model.predict_proba(input_data)
        churn_prob = probability[0][1]
        st.write("Churn Probability:", round(churn_prob*100,2), "%")
    except:
        pass

    if prediction[0] == 1:
        st.error("⚠️ Customer will leave the bank")
    else:
        st.success("✅ Customer will stay with the bank")
