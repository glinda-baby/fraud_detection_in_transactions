# **📌END-TO-END FINANCIAL FRAUD DETECTION SYSTEM USING SVM & STREAMLIT** #

## OVERVIEW ##

_This project presents an end-to-end Machine Learning solution for detecting fraudulent financial transactions. The system is designed to accurately classify transactions as fraudulent or legitimate using supervised learning techniques. The final model achieved 96.54% accuracy and was deployed as an interactive web application using Streamlit._

## PROBLEM STATEMENT ##

_Financial institutions face significant losses due to fraudulent transactions. The objective of this project is to build a predictive model that:_ 

 - _Accurately detects fraudulent transactions_
 - _Minimizes false negatives (critical for fraud prevention)_
 - _Can be deployed for real-time prediction_

## APPROACH ##

### 1️) Data Preprocessing ###
 - _Handled missing values_
 - _Feature engineering_
 - _Applied MinMax Scaling for normalization_
 - _Train-test split for evaluation_

### 2️) Model Experimentation ###

 - _Based on evaluation metrics, SVM showed superior performance._

### 3️) Final Model ###

 - **Algorithm**: _Support Vector Machine (SVM)_
 - **Accuracy**: _96.54%_
 - _Strong fraud detection capability with low false negatives_

## MODEL PERFORMANCE ##

### Confusion Matrix: ###

|                | Predicted: Not Fraud | Predicted: Fraud |
|----------------|---------------------|------------------|
| **Actual: Not Fraud** | 9810 | 328 |
| **Actual: Fraud**     | 190  | 4672 |

_The model demonstrates strong predictive capability while effectively reducing fraud misclassification._

## DEPLOYMENT ##

_The trained model was:_
 - _Serialized using Joblib_
 - _Integrated into a Streamlit web application_
 - _Designed for real-time transaction input and prediction_

## TECH STACK ##

 - _Python_
 - _scikit-learn_
 - _Pandas_
 - _NumPy_
 - _MinMaxScaler_
 - _Support Vector Machine (SVM)_
 - _Streamlit_
 - _Joblib_

## CONCLUSION ##
_Thank you for taking the time to explore this project. I hope it will be useful and insightful for anyone interested in prediction of Fraudulent Transactions._

_Contributions, suggestions, and improvements are always welcome!_ 

_Feel free to open an issue or submit a pull request to help enhance this repository._
  
  








