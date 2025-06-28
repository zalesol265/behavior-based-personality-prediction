
# 🧠 Personality Prediction from Behavioral Traits

This machine learning project predicts a person's personality type (e.g., introvert vs. extrovert) using self-reported behavioral traits. By analyzing factors like time spent alone, social event attendance, and social media activity, multiple classification models were trained and evaluated for performance and interpretability.

---

## 📁 Project Structure

```
├── src/
│   └── cleaning.py        # Data loading and outlier handling
├── notebooks/
│   └── 01_eda.ipynb
│   └── 02_modeling.ipynb
├── data/
│   └── personality_dataset.csv
├── README.md
└── requirements.txt
```

---

## 📊 Problem Statement

**Can we predict personality types using common behavioral indicators?**

This project explores the relationship between social behaviors and personality labels using a structured dataset of individuals’ activity patterns and self-perceptions.

---

## 🧼 Data Preprocessing

* Handled missing values and unnecessary labels
* Removed outliers **within each personality group** using IQR logic
* Scaled numeric features for consistent model input
* Explored correlation between variables (see heatmap)

---

## ⚙️ Features Used

| Feature                     | Description                                      |
| --------------------------- | ------------------------------------------------ |
| `Time_spent_Alone`          | Hours spent alone per day                        |
| `Social_event_attendance`   | Events attended per week                         |
| `Going_outside`             | Frequency of outdoor activity                    |
| `Friends_circle_size`       | Count of close friends                           |
| `Post_frequency`            | Social media activity level                      |
| `Stage_fear`                | Binary indicator of public speaking anxiety      |
| `Drained_after_socializing` | Binary indicator of energy loss post-socializing |

---

## 🤖 Models Trained

| Model                  | Accuracy  |
| ---------------------- | --------- |
| Logistic Regression    | 91.7%     |
| Support Vector Machine | **92.4%** |
| K-Nearest Neighbors    | **92.4%** |
| Random Forest          | 90.9%     |
| XGBoost                | 91.0%     |

* All models performed consistently well with accuracies above 90%.
* Simpler models like **SVM** and **KNN** performed on par with ensemble methods.

---

## 🔍 Feature Importance

| Model               | Top Features Identified                                       |
| ------------------- | ------------------------------------------------------------- |
| Logistic Regression | `Stage_fear`, `Drained_after_socializing`, `Post_frequency`   |
| Random Forest       | `Stage_fear`, `Time_spent_Alone`, `Drained_after_socializing` |
| XGBoost             | `Stage_fear`, `Time_spent_Alone`, `Drained_after_socializing` |
| KNN (Permutation)   | `Time_spent_Alone`, `Friends_circle_size` (minor importance)  |

The models consistently ranked **Stage Fear** and **Social Fatigue** as the most predictive traits, aligning well with psychological literature on introversion/extroversion.

---

## 📈 Visual Highlights

* Correlation heatmaps for understanding variable relationships
* Bar plots of feature importances across models
* Accuracy comparison charts for quick model evaluation

---

## ✅ Conclusion

This project demonstrates that personality traits can be reliably predicted using common behavioral metrics. Even without complex feature engineering, models like SVM and Logistic Regression achieved strong performance.

---

## 🔮 Future Work

Potential enhancements:

* Use SHAP or LIME for deeper interpretability
* Test with new behavioral features or survey data
* Deploy a web app for interactive predictions

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

