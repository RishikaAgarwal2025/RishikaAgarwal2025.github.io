---
layout: archive
title: "Academic Projects"
permalink: /projects/
author_profile: false
---


Below is a curated list of academic and applied projects, covering data analytics, forecasting, optimization, simulation modeling, A/B testing, and business analysis. Each project includes code, datasets, reports, and insights gained.

---

## 1. Forecasting Tata Motors' Stock Price using Nifty 50

This project involved building a time series forecasting model to predict Tata Motors’ stock price based on trends in the Nifty 50 index. Using ARIMA modeling in Stata, I performed stationarity testing, applied double differencing, and selected the optimal model using the Bayesian Information Criterion (BIC). The analysis, based on annual average closing prices from 2012 to 2022, forecasts a temporary decline in 2024 followed by a long-term upward trend. This work demonstrates my ability to apply statistical modeling techniques to uncover macroeconomic influences on firm-level performance, with hands-on experience in data preprocessing (Excel), model evaluation, and time series forecasting.

**Files**:
- [Forecasting Code](../assets/Time%20series%20econometrics/Forecasting%20code.txt)
- [Research Paper (PDF)](../assets/Time%20series%20econometrics/Forecasting_stock_market.pdf)
- [Dataset](../assets/Time%20series%20econometrics/Tata_motors_Nifty50.xlsx)


---

## 2 Data Management – SQL Simulation for Subscription Business

This project models a fictional subscription-based magazine company (BABA) to simulate real-world business operations using synthetic data. I designed a relational database schema to capture customer demographics, subscription details, payment activity, and engagement behavior. Using Python libraries like faker and pandas, I generated realistic fake data for thousands of records, enabling robust SQL querying and analysis.

The goal was to demonstrate how even simulated data can be used to derive actionable insights—such as revenue trends, churn behavior, and high-value customer segments. SQL was used to write complex queries that mimic real business questions, including customer retention metrics, cohort analysis, and engagement patterns across regions and product types. This project highlights my ability to integrate data engineering (schema design, data simulation) with business analytics (insight extraction, KPI generation), even in data-constrained environments.

**Files**: 
- [Faker Python Code](/assets/Data%20Management/Code/Fake%20data%20code.py)
- [Project Report (PDF)](/assets/Data%20Management/Report/Data%20Management_Report.pdf)


---

## 4. Treatment Control Testing (A/B Test)

**Description**: Evaluates the effectiveness of a new loan review model vs. existing model in a consumer lending company via an A/B test.

**Files**:
- [HTML Output](../assets/Treatment_Control_Testing/Code/Treatment_control_testing.html)
- [Report (PDF)](../assets/Treatment_Control_Testing/Report/Treatment_Control_Testing_Report.pdf)
- [Dataset](../assets/Treatment_Control_Testing/Data/Data.csv)

**Skills**: A/B testing, statistical inference  
**Tools**: R, MS Word  
**Key Insights**: The new model reduces Type I/II errors. Improvements in experiment design and dataset size are recommended for stronger inference.

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
