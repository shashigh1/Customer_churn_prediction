# 🧠 Customer Churn Prediction

A deep learning-powered web application that predicts whether a customer is likely to churn based on key banking and demographic features. Built with **Streamlit** for real-time user interaction and backed by a neural network model developed in **TensorFlow**.

🌐 **Live App**: [Launch the Web App](https://customer-churn-prediction-skk.streamlit.app/)

---

## 📌 Project Overview

This application enables businesses to proactively identify customers who are at risk of leaving, using historical data and advanced predictive analytics. The tool is easy to use, requiring only a few customer inputs to generate a prediction with confidence scores.

---

## 🎯 Key Features

✅ User-friendly web interface powered by Streamlit  
✅ Real-time prediction using a trained Artificial Neural Network (ANN)  
✅ Preprocessing includes feature scaling, label encoding, and one-hot encoding  
✅ Model trained and optimized in Google Colab using early stopping and validation   
✅ Outputs both churn prediction and probability score  

---

## 🧠 Model Summary

- Trained on structured customer data using an **Artificial Neural Network (ANN)**
- Optimized with the **Adam** optimizer and **binary cross-entropy** loss
- Includes **early stopping** for efficient training and to prevent overfitting
- Achieves high accuracy on the validation set

---

## 🏗️ Architecture

**Frontend**:  
- Streamlit form-based interface for customer data input and prediction display

**Backend**:  
- `model.keras` – Trained TensorFlow model  
- `ss.pkl` – Scikit-learn StandardScaler for numerical features  
- `label_encoder.pkl` – LabelEncoder for gender  
- `ohe_geo.pkl` – OneHotEncoder for geography  

---

## ✅ Prediction Output

- **Churn Probability**: A float value between 0 and 1 (e.g., `0.84`)
- **Prediction Decision**:
  - ⚠️ **Customer is likely to churn**
  - ✅ **Customer is not likely to churn**

