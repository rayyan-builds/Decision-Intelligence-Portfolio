# Customer Personality Analysis Using Machine Learning

> Using customer data and machine learning to predict spending behavior and identify customers most likely to respond to marketing campaigns.

## Project Overview

This project applies **Machine Learning and Business Analytics** to customer data to understand purchasing behavior and improve marketing decision-making.

Using the **Customer Personality Analysis dataset containing 2,240 customer records**, the project addresses two predictive analytics problems:

- **Regression:** Predict customer `Total_Spending`
- **Classification:** Predict whether a customer will respond positively to a marketing campaign

The project follows an end-to-end machine learning workflow covering **Exploratory Data Analysis, feature engineering, preprocessing, model training, evaluation, and business interpretation**. 

## Key Questions

The analysis focuses on questions such as:

- Which customer characteristics are associated with higher spending?
- Can customer spending be predicted from demographic and behavioral information?
- Which customers are more likely to respond to marketing campaigns?
- Which machine learning models perform best for each prediction task?
- How can these predictions support customer targeting and marketing decisions?

## Approach

### 1. Data Preparation
- Investigated data quality and missing values
- Applied median imputation to missing income values
- Checked duplicate records
- Encoded categorical variables
- Engineered features such as Age, Children, and Total Purchases
- Applied feature scaling using `StandardScaler`
- Used an 80/20 train-test split
- Removed spending variables from regression features to prevent target leakage

### 2. Exploratory Data Analysis

The analysis examined:

- Customer spending distributions
- Campaign response distribution
- Correlations between customer characteristics and spending
- Income vs. total spending
- Education level vs. spending behavior
- Customer purchasing and engagement patterns

### 3. Machine Learning

#### Regression Models
- Linear Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN) Regressor

#### Classification Models
- Logistic Regression
- KNN Classifier
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

## Results

The **Random Forest Regressor** achieved the strongest regression performance, with an **R² score of 0.8795**, outperforming the other regression models. It was particularly effective at capturing non-linear relationships between income, purchasing behavior, and customer characteristics. :contentReference[oaicite:1]{index=1}

For classification, the **Random Forest Classifier** produced the strongest overall performance across the evaluated metrics. Because the campaign-response data was imbalanced, **Precision, Recall, and F1 Score** were considered alongside Accuracy rather than relying on Accuracy alone. :contentReference[oaicite:2]{index=2}

## Business Insights

The analysis suggests that:

- Higher-income customers generally tend to spend more.
- Purchasing activity and customer engagement are important indicators of spending behavior.
- Predictive models can help identify customers more likely to respond to campaigns.
- Machine learning can support **customer segmentation, personalized targeting, campaign optimization, customer retention, and revenue-related decision-making**. :contentReference[oaicite:3]{index=3}

## Project Files

| File | Description |
|---|---|
| `Python____.ipynb` | Main analysis notebook containing the data preparation, exploratory analysis, feature engineering, machine learning models, evaluation, and visualizations. |
| `ML_Project Report.pdf` | Detailed project report documenting the dataset, methodology, model comparisons, results, business insights, limitations, and conclusions. |

## Tools & Technologies

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Matplotlib` · `Seaborn` · `Jupyter Notebook`

## Business Application

The project demonstrates how predictive analytics can move beyond descriptive reporting toward **data-driven customer and marketing decisions**.

The resulting models can be used as a foundation for identifying high-value customers, prioritizing marketing campaigns, improving customer targeting, and supporting customer relationship management.

## Limitations

The classification dataset contained a significant class imbalance, and advanced hyperparameter optimization was not performed. The dataset also represents a particular customer context, so the models may not generalize directly to every industry or business environment. :contentReference[oaicite:4]{index=4}

---

### Skills Demonstrated

**Data Analytics | Exploratory Data Analysis | Feature Engineering | Predictive Modeling | Classification | Regression | Model Evaluation | Business Analytics | Customer Analytics | Marketing Analytics**
