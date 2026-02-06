# SMS Spam Classifier (Adversarially Robust)

A machine learning project that builds and stress-tests an SMS spam classifier using real-world data.

## 🔍 Problem
Spam detection is an adversarial problem where attackers actively obfuscate text to evade filters.

## 🧠 Approach
- Exploratory Data Analysis (EDA)
- TF-IDF feature extraction
- Logistic Regression with class imbalance handling
- Character n-grams for robustness
- Domain-aware normalization (e → 3, a → @)
- Adversarial stress testing

## 🛠 Techniques Used
- TF-IDF (word & character level)
- Logistic Regression
- Feature engineering
- Distribution shift analysis
- Adversarial testing

## 📈 Results
- Spam Recall: ~94%
- Spam Precision: ~94%
- Improved robustness against obfuscated spam (e.g. `Fr33 c@sh w1n n0w`)

## 📂 Dataset
SMS Spam Collection Dataset (UCI Machine Learning Repository)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/train.py
