![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/svarshini540-jpg/product-review-sentiment-analysis)
![Build Status](https://github.com/svarshini540-jpg/product-review-sentiment-analysis/actions/workflows/python-ci.yml/badge.svg)

# Product Review Sentiment Analysis

This project is an end-to-end Machine Learning application that classifies product reviews as **positive** or **negative** using Natural Language Processing (NLP).

---

## Project Structure

product-review-sentiment-analysis/
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned dataset
├── src/
│ ├── preprocess.py # Text preprocessing script
│ └── train_and_evaluate.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

---

## Dataset

The project uses the **IMDB Movie Reviews dataset**, which contains labeled text reviews for sentiment classification.

---

## Workflow

1. Load raw review data  
2. Clean and preprocess text  
3. Convert text into numerical features using **TF-IDF**  
4. Train a **Logistic Regression** model  
5. Evaluate model performance  

---

## How to Run the Project

pip install -r requirements.txt
python src/preprocess.py
python src/train_and_evaluate.py
---
Model Details

Algorithm: Logistic Regression

Feature Extraction: TF-IDF Vectorizer

Evaluation Metrics: Accuracy, Precision, Recall
---
Results

The trained model predicts whether a given review is positive or negative with good accuracy.
---
Future Improvements

Use deep learning models such as LSTM or BERT

Add a web interface using Flask or Streamlit

Perform hyperparameter tuning
