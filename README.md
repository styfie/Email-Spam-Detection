# 📧 Spam Email Classifier

A minimalistic machine learning app to classify email or message text as **Spam** or **Ham**, built using **Streamlit**, **scikit-learn**, and a trained model from the **UCI SMS Spam Collection Dataset**.

---

## 📊 Dataset

This project uses the **UCI SMS Spam Collection Dataset**, a well-known benchmark dataset consisting of **5,574 labeled SMS messages**, divided into:

* **ham** → legitimate (non-spam) messages
* **spam** → unsolicited, promotional, or fraudulent messages

---

## 🧠 Function of the Spam Detection Model

The machine learning model analyzes input text and predicts whether the message is **Spam** or **Ham** based on:
* Keyword frequency
* TF-IDF vector patterns
* Statistical patterns commonly seen in spam messages

This enables fast text screening for:
* Email filtering
* SMS moderation
* Basic content risk assessment

The model is trained using **TF-IDF Vectorization** combined with a **Machine Learning classifier** (Support Vector Machine).

---

## 🖥️ Live Demo

*https://styfiespamdetection.streamlit.app/*

