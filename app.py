import streamlit as st
import pandas as pd
import pickle

# load model and scaler
model = pickle.load(open("model.pkl","rb"))

st.title("🏦 Bank Customer Churn Prediction")

st.write("Enter customer details to check if the customer will leave the bank.")

# Inputs
credit_score = st.number_input("Credit Score",300,900,600)
age = st.slider("Age",18,100,35)
tenure = st.slider("Tenure",0,10,3)
balance = st.number_input("Balance",0.0,250000.0,50000.0)
num_products = st.slider("Number of Products",1,4,1)
has_credit_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])
estimated_salary = st.number_input("Estimated Salary",0.0,200000.0,50000.0)

geography = st.selectbox("Geography",["France","Germany","Spain"])
gender = st.selectbox("Gender",["Male","Female"])

# Encoding
geo_germany = 1 if geography=="Germany" else 0
geo_spain = 1 if geography=="Spain" else 0
gender_male = 1 if gender=="Male" else 0

# DataFrame
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

# scale input


if st.button("Predict"):

    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    st.write("Churn Probability:", round(prob[0][1]*100,2), "%")

    if prediction[0] == 1:
        st.error("⚠️ Customer will leave the bank")
    else:
        st.success("✅ Customer will stay with the bank")
