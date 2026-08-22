# Customer Personality Analysis

> Predictive customer analytics using machine learning to understand spending behaviour and marketing campaign response.

**Python** · **Scikit-learn** · **Pandas** · **Machine Learning** · **Customer Analytics** · **Marketing Analytics**

---

## Business Problem

Businesses collect large amounts of customer demographic, purchasing, web activity, and campaign data, but raw customer data alone does not explain which customers are likely to spend more or respond to marketing campaigns.

This project applies machine learning to address two business problems:

1. **How accurately can customer spending behaviour be predicted?**
2. **Can customers likely to respond positively to a marketing campaign be identified?**

The objective was not only to compare machine learning models, but to translate their results into insights relevant to customer segmentation, targeted marketing, and business decision-making.

---

## Key Results

| Area | Result |
|---|---|
| Dataset | **2,240 customer records** |
| Regression Task | Predict customer total spending |
| Best Regression Model | **Random Forest Regressor** |
| Best Regression R² | **0.8795** |
| Weakest Regression R² | **0.1120 — SVR** |
| Classification Task | Predict positive campaign response |
| Best Classification Model | **Random Forest Classifier** |

The Random Forest Regressor substantially outperformed the other regression approaches, capturing complex non-linear relationships in customer spending behaviour.

For classification, Random Forest produced the strongest overall balance across the evaluated metrics. Because the campaign-response data was imbalanced, F1 Score was considered alongside accuracy, precision, and recall rather than relying on accuracy alone.

---

## What I Built

An end-to-end customer analytics workflow covering:

**Data → EDA → Preprocessing → Feature Engineering → Model Training → Model Comparison → Business Insights**

The project included:

- Exploratory Data Analysis
- Data quality assessment
- Missing-value treatment
- Duplicate checking
- Categorical variable encoding
- Feature engineering
- Feature selection
- Feature scaling
- Regression modelling
- Classification modelling
- Model evaluation
- Business interpretation

Target leakage was also considered when preparing the regression features.

---

## Machine Learning Approach

### Regression

Five regression models were developed and compared:

- Linear Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN) Regressor

**Evaluation metrics:**

`MAE` · `MSE` · `RMSE` · `R²`

### Classification

Five classification models were evaluated:

- Logistic Regression
- KNN Classifier
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

**Evaluation metrics:**

`Accuracy` · `Precision` · `Recall` · `F1 Score`

---

## Why Random Forest Performed Best

The Random Forest Regressor achieved an **R² of 0.8795**, substantially outperforming SVR at **0.1120**.

This indicates that the ensemble approach was better able to capture the non-linear relationships between customer characteristics, purchasing behaviour, and spending.

For classification, Random Forest achieved the strongest overall performance, while the Decision Tree model showed stronger recall in identifying positive campaign responders. This illustrates an important business trade-off: the "best" model can depend on whether a company prioritizes overall predictive balance or identifying as many potential responders as possible.

---

## Business Insights

The analysis identified relationships between:

- Customer income
- Purchasing activity
- Customer engagement
- Recency
- Spending behaviour
- Marketing campaign response

One notable finding was that higher-income customers tended to demonstrate higher spending behaviour.

The analysis also showed that purchasing activity and customer engagement patterns provide useful signals for understanding customer spending.

These findings can support:

- **Customer segmentation**
- **Targeted marketing**
- **Personalized campaigns**
- **High-value customer identification**
- **Customer retention**
- **Revenue-related forecasting**
- **Data-driven marketing decisions**

---

## Business Value

The project demonstrates how machine learning can move customer analytics beyond simply describing what happened.

Instead, historical customer data can be used to answer questions such as:

> **Who is likely to spend more?**

> **Who is more likely to respond to a campaign?**

> **Which customer characteristics provide useful predictive signals?**

This creates a foundation for more targeted allocation of marketing resources and more informed customer relationship decisions.

---

## Project Workflow

```text
Customer Dataset
       ↓
Data Quality Assessment
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering & Selection
       ↓
Data Preprocessing & Scaling
       ↓
Train / Test Split
       ↓
Regression + Classification
       ↓
Model Evaluation & Comparison
       ↓
Business Insights
