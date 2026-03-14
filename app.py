import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl","rb"))

st.title("Bank Customer Churn Prediction")

credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
tenure = st.number_input("Tenure")
balance = st.number_input("Balance")
num_products = st.number_input("Number of Products")
has_credit_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])
estimated_salary = st.number_input("Estimated Salary")

geography = st.selectbox("Geography",["France","Germany","Spain"])
gender = st.selectbox("Gender",["Male","Female"])

# convert categorical variables
geo_germany = 1 if geography=="Germany" else 0
geo_spain = 1 if geography=="Spain" else 0
gender_male = 1 if gender=="Male" else 0

# dataframe with SAME order as training
input_data = pd.DataFrame([[
credit_score,
geo_germany,
geo_spain,
gender_male,
age,
tenure,
balance,
num_products,
has_credit_card,
is_active_member,
estimated_salary
]],columns=[
'CreditScore',
'Geography_Germany',
'Geography_Spain',
'Gender_Male',
'Age',
'Tenure',
'Balance',
'NumOfProducts',
'HasCrCard',
'IsActiveMember',
'EstimatedSalary'
])

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0]==1:
        st.error("Customer will leave the bank")
    else:
        st.success("Customer will stay")
