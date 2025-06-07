---
layout: archive
title: "Academic Projects"
permalink: /projects/
author_profile: false
---


Below is a curated list of academic and applied projects, covering data analytics, forecasting, optimization, simulation modeling, A/B testing, and business analysis. Each project includes code, datasets, reports, and insights gained.

---

## 1. Forecasting Tata Motors' Stock Price using Nifty 50

Tools: Stata, Excel

This project involved building a time series forecasting model to analyze the relationship between Tata Motors’ stock price and the Nifty 50 index. I performed stationarity testing, applied double differencing, and selected the optimal ARIMA model using the Bayesian Information Criterion (BIC). The model, based on annual average closing prices from 2012 to 2022, forecasts a temporary decline in 2024 followed by a long-term upward trend.
This work highlights my ability to use statistical modeling techniques to understand macroeconomic influences on firm-level performance.

**Files**:
- [Forecasting Code](../assets/Time%20series%20econometrics/Forecasting%20code.txt)
- [Research Paper (PDF)](../assets/Time%20series%20econometrics/Forecasting_stock_market.pdf)
- [Dataset](../assets/Time%20series%20econometrics/Tata_motors_Nifty50.xlsx)


---

## 2. Data Management – SQL Simulation for Subscription Business

**Tools**: Python (faker, pandas), SQL

To simulate real-world business scenarios, I designed a relational database for a fictional magazine subscription company. The schema captured customer demographics, subscriptions, payments, and engagement data. Using Python, I generated realistic synthetic data and used SQL to perform complex queries mimicking actual business questions.
Insights derived include churn rates, revenue trends, and customer lifetime value across different regions and product tiers. This project combines data engineering and business analytics to derive actionable insights in data-constrained environments.

**Files**: 
- [Faker Python Code](/assets/Data%20Management/Code/Fake%20data%20code.py)
- [Project Report (PDF)](/assets/Data%20Management/Report/Data%20Management_Report.pdf)


---

## 3. Evaluating a Loan Review Model via A/B Testing

**Tools**: R

This project evaluated a new loan review model using an A/B testing framework within a consumer lending firm. By comparing error rates (Type I and II) between treatment (new model) and control (existing system) groups, the analysis showed that the new model significantly reduced both false approvals and rejections.
The project also identifies areas for improving the experimental design like better group balancing and increasing sample size. It demonstrates practical use of hypothesis testing, experimental data analysis, and clear interpretation of results for business impact.

**Files**: 
- [HTML Output](/assets/Treatment%20control%20testing/Code/Treatment%20control%20testing.html)
- [Report (PDF)](/assets/Treatment%20control%20testing/Report/Treatment%20Control%20Testing%20Report.pdf)
- [Dataset](/assets/Treatment%20control%20testing/Data/Data.csv)


---

## 5. Pricing Analytics for BuildMax Rentals

**Description**: Uses linear programming to optimize equipment pricing and fleet allocation for BuildMax Rentals based on historical rental data.

**Files**:
- [Python Code](../assets/Pricing_Analytics/Copy.py)
- [Report (PDF)](../assets/Pricing_Analytics/Report.pdf)
- [Dataset](../assets/Pricing_Analytics/BuildMax_Rentals_Updated.xlsx)

**Skills**: Optimization modeling, pricing strategy  
**Tools**: Python (Pyomo), MS PowerPoint  
**Key Insights**: Recommends balancing short- and long-term rentals, improving demand granularity, and refining maintenance & pricing strategies for revenue gain.

---

## 6. Analytics in Practice – Brazilian E-commerce Dataset

**Description**: Builds predictive models to identify customers likely to leave positive reviews for the e-commerce platform Nile.

**Files**:
- [Python Code](../assets/Analysis_in_Practice/AIP_code.ipynb)
- [Report (PDF)](../assets/Analysis_in_Practice/AIP_report.pdf)
- [Presentation](../assets/Analysis_in_Practice/AIP_presentation.pdf)
- [Dataset Sample](../assets/Analysis_in_Practice/brazilian-ecommerce-dataset/olist_orders_dataset.csv)

**Skills**: Machine learning, customer analytics  
**Tools**: Python (XGBoost, Logistic Regression, SVM), PowerPoint  
**Key Insights**: Gradient Boosting performed best. Recommended further feature engineering and class balancing to improve predictive power.

---

## 7. Business Statistics with R

**Description**: Analyzes datasets on street foot traffic, cardiovascular disease, and retail customer satisfaction to derive actionable insights.

**Files**:
- [RMarkdown Code 1](../assets/Business_Statistics/Assignment_1/Code/Business_Statistics_Assignment1.md)
- [RMarkdown Code 2](../assets/Business_Statistics/Assignment_2/Code/Code_Assignment.Rmd)
- [Datasets](../assets/Business_Statistics/Assignment_2/Dataset/cust_satisfaction.csv)

**Skills**: Statistical modeling, data visualization, reproducible reporting  
**Tools**: R  
**Key Insights**:
  - Consistent footfall observed in Coney Street.
  - Smoking, weight, and wellness are key CVD predictors.
  - Customer satisfaction linked strongly to staff service, delivery time, and SES.

---

## 8. Understanding Business for Analysts – Case Study on MyProtein

**Description**: Uses the DELTA framework to assess MyProtein’s data strategy. Includes stakeholder analysis, risk planning, and AI-driven personalization proposals.

**Files**:
- [Report (PDF)](../assets/Understanding_Business_for_Analysts/Report-UBFA.pdf)

**Skills**: Strategic analysis, stakeholder evaluation, business interpretation  
**Tools**: MS Word, MS PowerPoint  
**Key Insights**: MyProtein shows strong data use but needs better scalability. Recommends small-scale AI pilot programs with feedback loops to reduce bias and enhance customer engagement.
