import streamlit as st
import pandas as pd
import pickle


# ===============================
# Load Model
# ===============================
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.set_page_config(page_title="Fraud Detection System")

st.title("💳 Fraud Detection System")
st.write("Enter transaction details below:")

# ===============================
# Numerical Inputs
# ===============================

transaction_amount = st.number_input("Transaction Amount", min_value=0.0)
account_balance = st.number_input("Account Balance", min_value=0.0)
previous_fraud = st.selectbox("Previous Fraudulent Activity", [0, 1])
daily_transaction_count = st.number_input("Daily Transaction Count", min_value=0)
avg_transaction_7d = st.number_input("Average Transaction Amount (7 days)", min_value=0.0)
failed_txn_7d = st.number_input("Failed Transaction Count (7 days)", min_value=0)
card_age = st.number_input("Card Age (months)", min_value=0)
risk_score = st.number_input("Risk Score", min_value=0.0)

# ===============================
# Categorical Inputs
# ===============================

transaction_type = st.selectbox("Transaction Type",
                                ["Bank Transfer", "Online", "POS"])

device_type = st.selectbox("Device Type",
                           ["Mobile", "Tablet"])

location = st.selectbox("Location",
                        ["Mumbai", "New York", "Sydney", "Tokyo"])

merchant_category = st.selectbox("Merchant Category",
                                 ["Electronics", "Groceries",
                                  "Restaurants", "Travel"])

card_type = st.selectbox("Card Type",
                         ["Discover", "Mastercard", "Visa"])

authentication_method = st.selectbox("Authentication Method",
                                     ["OTP", "PIN", "Password"])

# ===============================
# Prediction
# ===============================

if st.button("Predict Fraud"):

    # Create dataframe
    input_data = pd.DataFrame({
        "Transaction_Amount": [transaction_amount],
        "Account_Balance": [account_balance],
        "Previous_Fraudulent_Activity": [previous_fraud],
        "Daily_Transaction_Count": [daily_transaction_count],
        "Avg_Transaction_Amount_7d": [avg_transaction_7d],
        "Failed_Transaction_Count_7d": [failed_txn_7d],
        "Card_Age": [card_age],
        "Risk_Score": [risk_score],
        "Transaction_Type": [transaction_type],
        "Device_Type": [device_type],
        "Location": [location],
        "Merchant_Category": [merchant_category],
        "Card_Type": [card_type],
        "Authentication_Method": [authentication_method]
    })

    # Apply same encoding
    input_encoded = pd.get_dummies(input_data)

    # Add missing columns
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    # Ensure same column order
    input_encoded = input_encoded[model_columns]

    # Predict
    prediction = model.predict(input_encoded)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")