🧠 Customer Churn Prediction
A Deep learning-powered web application that predicts whether a customer is likely to churn based on key banking and demographic features. Built with Streamlit for real-time user interaction and backed by a deep learning model developed in TensorFlow.

📌 Project Overview
This application enables businesses to proactively identify customers who are likely to leave, using historical data and advanced predictive analytics. The tool is simple to use, requiring only a few customer inputs to generate a prediction.

🎯 Key Features
✅ User-friendly web interface powered by Streamlit

✅ Real-time prediction using a trained neural network (ANN)

✅ Preprocessing includes scaling, label encoding, and one-hot encoding

✅ Model trained and optimized in Google Colab with early stopping and validation


🧠 Model Summary
Trained on structured customer data using an Artificial Neural Network (ANN)

Optimized using the Adam optimizer and binary cross-entropy loss

Includes early stopping for efficient training and overfitting prevention

Achieves high accuracy on validation data

🏗️ Architecture
Frontend: Streamlit form-based interface for data input and result visualization

Backend:

TensorFlow model (model.keras) for prediction

StandardScaler (ss.pkl) for feature scaling

LabelEncoder (label_encoder.pkl) for categorical gender data

OneHotEncoder (ohe_geo.pkl) for geography data


✅ Prediction Output
Churn Probability: Value between 0 and 1

Decision:
  ⚠️ Customer is likely to chur
  ✅ Customer is not likely to churn
⚠️ Customer is likely to churn

✅ Customer is not likely to churn
