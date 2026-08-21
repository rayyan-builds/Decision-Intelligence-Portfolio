# Customer Personality Analysis Using Machine Learning

A predictive customer analytics project that uses machine learning to understand customer spending behavior and predict responses to marketing campaigns.

## Project Overview

This project applies an end-to-end machine learning workflow to the **Customer Personality Analysis** dataset, containing 2,240 customer records with demographic, purchasing, web activity, and marketing campaign information.

The analysis focuses on two business problems:

- Predicting **customer total spending**
- Predicting whether a customer will **respond positively to a marketing campaign**

The project demonstrates how predictive analytics can support **customer segmentation, targeted marketing, customer retention, and data-driven decision-making**.

## Key Objectives

- Predict `Total_Spending` using customer characteristics and purchasing behavior.
- Predict customer response to marketing campaigns.
- Compare multiple machine learning algorithms.
- Identify important patterns in customer demographics, income, purchasing activity, and engagement.
- Translate machine learning results into practical business insights.

## Methodology

The project follows a complete predictive analytics workflow:

1. Exploratory Data Analysis
2. Data quality assessment
3. Missing-value treatment
4. Duplicate checking
5. Categorical variable encoding
6. Feature engineering
7. Feature selection
8. Feature scaling using `StandardScaler`
9. 80/20 train-test split
10. Regression model training and comparison
11. Classification model training and comparison
12. Model evaluation
13. Business interpretation

Target leakage was addressed by removing spending-related variables used to create `Total_Spending` from the regression features.

## Machine Learning Models

### Regression

- Linear Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN) Regressor

### Classification

- Logistic Regression
- KNN Classifier
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM) Classifier

### Evaluation Metrics

**Regression**

- MAE
- MSE
- RMSE
- R² Score

**Classification**

- Accuracy
- Precision
- Recall
- F1 Score

## Key Results

The **Random Forest Regressor** was the strongest regression model, achieving an **R² Score of approximately 0.8795**.

For classification, the **Random Forest Classifier** achieved the strongest overall performance among the tested models. Due to the imbalance between positive and negative campaign responses, **F1 Score** was considered particularly important alongside other classification metrics.

## Business Insights

The analysis identified meaningful relationships between:

- Customer income
- Purchasing activity
- Recency
- Customer engagement
- Total spending
- Marketing campaign responses

Higher-income customers generally demonstrated higher spending behavior, while purchasing and engagement patterns also provided useful signals for customer analysis.

The results can support:

- **Customer segmentation**
- **Personalized marketing**
- **Campaign targeting**
- **Customer retention**
- **Revenue forecasting**
- **Identification of high-value customers**
- **Data-driven marketing decisions**

The analysis also highlights the business cost of **false negatives**, where potentially responsive customers may be incorrectly classified as non-responders.

## Project Files

| File | Description |
|---|---|
| `Dataset.xlsx` | Customer Personality Analysis dataset containing demographic, purchasing, engagement, and campaign-response information. |
| `Python_File.ipynb` | Main analysis notebook containing data preparation, exploratory analysis, feature engineering, machine learning models, evaluation, and visualizations. |
| `ML_Project Report(1).pdf` | Detailed project report documenting the dataset, methodology, model comparisons, results, business insights, limitations, and conclusions. |

## Tools & Technologies

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Matplotlib` · `Seaborn` · `Jupyter Notebook` · `Excel`

## Business Application

The project demonstrates how predictive analytics can move beyond descriptive analysis toward **data-driven customer and marketing decisions**.

The resulting models provide a foundation for identifying high-value customers, prioritizing marketing campaigns, improving customer targeting, and supporting customer relationship management.

## Limitations

- The classification dataset contains a significant class imbalance.
- Advanced hyperparameter optimization was not performed.
- The dataset represents a specific customer context and may not generalize directly to every industry or business environment.

---

## Skills Demonstrated

**Data Analytics | Exploratory Data Analysis | Feature Engineering | Data Preprocessing | Predictive Analytics | Regression | Classification | Model Evaluation | Customer Analytics | Marketing Analytics | Business Decision Support**
