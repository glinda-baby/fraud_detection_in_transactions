# 👋 ABOUT ME #
### Hi, I'm Glinda Baby! ### 
- 💻 Aspiring Data Scientist  
- 🌱 Currently learning and experimenting with data, algorithms, deploying models and so on
- 🚀 I enjoy solving problems, contributing to projects, and collaborating with developers worldwide.  
- 🛠️ Passionate about solving real-world problems through data, algorithms, and innovation.  
- 📫 How to reach me: glindababy23@gmail.com
 
 *Always excited to learn, share, and grow with the developer community!* 


# 🔍ABOUT THIS REPOSITORY #
This repository showcases my project work in Machine Learning about the prediction of **Fraud Detection in Transactions**

The contents are:
- 🗒️ _Data set **Fraud_Detection_in_Transactions.csv**  which is used for analysis_  
- 🗒️ _Model deployed using Support Vector Machine Algorithm in VS Code_
- 🗒️ _App built using Streamlit_

# 🔍ABOUT THE DATASET #
## Fraud Detection in Transactions Dataset ## 
_The Fraud Detection in Transactions dataset is made for research and experimentation to identify fraudulent financial activities. It contains transaction level data that can help train, validate, and evaluate machine learning models for fraud detection._  

 ## DATASET SCHEMA

| Column Name                  | Data Type | Description |
|------------------------------|-----------|-------------|
| Transaction_ID               | object    | Unique identifier for each transaction |
| User_ID                      | object    | Unique identifier for each user |
| Transaction_Amount           | float64   | Amount involved in the transaction |
| Transaction_Type             | object    | POS, Bank Transfer, Online, ATM Withdrawal |
| Timestamp                    | object    | Date and time of the transaction |
| Account_Balance              | float64   | Account balance after the transaction |
| Device_Type                  | object    | Laptop, Mobile, Tablet |
| Location                     | object    | Sydney, New York, Mumbai, Tokyo, London |
| Merchant_Category            | object    | Travel, Clothing, Restaurants, Electronics, Groceries |
| IP_Address_Flag              | float64   | Indicator for suspicious IP usage |
| Previous_Fraudulent_Activity | float64   | Count of past fraudulent activities |
| Daily_Transaction_Count      | float64   | Number of transactions in a day |
| Avg_Transaction_Amount_7d    | float64   | Average transaction amount in the past 7 days |
| Failed_Transaction_Count_7d  | int64     | Failed transactions in the past 7 days |
| Card_Type                    | object    | Amex, Mastercard, Visa, Discover |
| Card_Age                     | int64     | Age of the card in years |
| Transaction_Distance         | float64   | Distance between transaction origin and user’s location |
| Authentication_Method        | object    | Biometric, Password, OTP, PIN |
| Risk_Score                   | float64   | Calculated risk score for the transaction |
| Is_Weekend                   | float64   | Flag indicating if transaction occurred on weekend |
| Fraud_Label                  | int64     | Target variable (1 = Fraud, 0 = Legitimate) |

## USE CASES ##
  - _Building and evaluating fraud detection models_  
  - _Testing anomaly detection algorithms_  
  - _Exploring feature engineering strategies for financial datasets_  

## WHY IT MATTERS ##  
_Fraudulent transactions present significant risks to businesses and consumers. By using this dataset, developers and researchers can try out methods to improve the accuracy of fraud detection, reduce false positives, and strengthen financial security systems._

# PLATFORM USED #
_Visual Studio Code (VS Code)_

# ALGORITHM IMPLEMENTED #
_Support Vector Machine Algorithm_
  
# PYTHON LIBRARIES USED #
 - _Numpy_
 - _Pandas_
 - _Matplotlib_
 - _Scikit-learn_

# WORKFLOW #
 - _importing required python libraries_
 - _Loading dataset_
 - _Data Preprocessing_
 - _Exploratory Data Analysis (EDA)_
 - _Encoding using get_dummies method_
 - _dropping unwanted columns_
 - _filling missing values_
 - _Seperating Input and Output_
 - _Train-Test Split_
 - _Normalisation using MinMaxScaler
 - _Model Creation_
 - _Performance Evaluation_

# CONCLUSION #
Thank you for taking the time to explore this project. I hope it will be useful and insightful for anyone interested in prediction of Fraudulent Transactions.
Contributions, suggestions, and improvements are always welcome!  
Feel free to open an issue or submit a pull request to help enhance this repository.
  
  **Together, we can continue to improve and build something even better.**








