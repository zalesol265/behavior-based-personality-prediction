# 🧠 Predicting Personality Type from Behavior Patterns

This project explores and predicts whether a person is an **Introvert** or **Extrovert** using behavioral survey data. It combines machine learning, data visualization, and exploratory analysis to uncover meaningful patterns and build a predictive model.

## 📁 Project Structure

```

personality-predictor/
├── README.md
├── data/
│   └── behavior\_data.csv
├── notebooks/
│   ├── 01\_eda.ipynb
│   ├── 02\_modeling.ipynb
│   └── 03\_dashboard.ipynb  (optional)
├── src/
│   ├── data\_cleaning.py
│   ├── modeling.py
│   └── visualization.py
├── requirements.txt
└── app/ (optional Streamlit dashboard)

````

## 🧰 Tech Stack

- Python (Pandas, NumPy, Scikit-learn, Seaborn, Plotly)
- Optional: Streamlit or Power BI
- Git/GitHub for version control

## 📊 Exploratory Data Analysis

- Group preferences, screen time, reading habits, etc.
- Correlation heatmaps
- t-SNE or PCA for visualization

## 🤖 Modeling

- Models used: Logistic Regression, Random Forest, XGBoost
- Evaluation: Accuracy, Confusion Matrix, F1-score
- Top features by importance

## 🌐 Dashboard (Optional)

- Streamlit app for personality prediction
- Form to input behavior responses
- Charts comparing introvert vs. extrovert traits

## 📌 Dataset

Data from [Kaggle](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)

## 🚀 Running Locally

```bash
git clone https://github.com/your-username/personality-predictor.git
cd personality-predictor
pip install -r requirements.txt
jupyter notebook
````

Or run the dashboard:

```bash
streamlit run app/app.py
```


