import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model & Columns

model=joblib.load("svm_fraud_model.pkl")
model_columns=joblib.load("model_columns.pkl")

# Page Config

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("Fraud Detection in Transactions 🚨")
st.write("Enter your transaction details to predict whether it is Fraud or Not Fraud.")

st.markdown("---")

# User Inputs 

transaction_amount = st.number_input("Transaction Amount", min_value=0.0, value=0.0)
Account_Balance = st.number_input("Account Balance", min_value=0.0,value=0.0)
Previous_Fraudulent_Activity = st.number_input("Number of Previous Fraudulent Activity", min_value=0.0,value=0.0)
Daily_Transaction_Count = st.number_input("Number of Transactions done in a day", min_value=0.0,value=0.0)
Avg_Transaction_Amount_7d = st.number_input("Average Transaction Amount in a week", min_value=0.0,value=0.0)
failed_transaction_count_7d = st.number_input("Number of Failed Transactions in a week", min_value=0, value=0)
Card_Age = st.number_input("Card age (in Months)", min_value=0, value=0)
risk_score = st.slider("Risk Score", 0.0, 1.0, 0.5)

# Example categorical
Transaction_Type = st.selectbox("Transaction Type", ["Bank Transfer", "Online", "POS"])
device_type = st.selectbox("Device Type", ["Mobile", "Tablet", "Desktop"])
Location = st.selectbox("Location", ["Mumbai", "New York", "Sydney", "Tokyo"])
Merchant_Category = st.selectbox("Merchant Category", ["Electronics", "Groceries", "Restaurants", "Travel"])
Card_Type = st.selectbox("Card Type", ["Discover", "Mastercard", "Visa"])
Authentication_Method = st.selectbox("Authentication Method", ["OTP", "PIN", "Password"])

# Create Input DataFrame
input_data = {
    "Transaction_Amount": transaction_amount,
    "Account Balance" : Account_Balance,
    "Number of Previous Fraudulent Activity" : Previous_Fraudulent_Activity,
    "Number of Transactions done in a day" : Daily_Transaction_Count,
    "Average Transaction Amount in a week" : Avg_Transaction_Amount_7d,
    "Number of Failed Transactions in a week" : failed_transaction_count_7d,
    "Card age (in Months)" : Card_Age,
    "Risk Score" : risk_score
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Encoding
input_df = pd.get_dummies(input_df)

# Add missing columns (very important)
for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns
input_df = input_df[model_columns]

# Prediction Button

if st.button("🔍 Predict Fraud"):

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

    st.write("Prediction Code:", prediction)