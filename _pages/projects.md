---
layout: archive
title: "Academic Projects"
permalink: /projects/
author_profile: false
---


Below is a curated list of academic and applied projects, covering data analytics, forecasting, optimization, simulation modeling, A/B testing, and business analysis. Each project includes code, datasets, reports, and insights gained.

---

## 1. Forecasting Tata Motors' Stock Price using Nifty 50

**Objective**:
This project investigates the predictive relationship between the Nifty 50 index and the average annual closing price of Tata Motors using ARIMA (AutoRegressive Integrated Moving Average) modeling techniques. The primary goal is to identify long-term trends and forecast the company's future stock performance over a 6-year horizon, based on historical data from 2012 to 2022.

**Overview**:
The study utilizes average annual closing prices to apply time series econometric methods, focusing on the dynamic interaction between Tata Motors’ stock price and the broader market represented by the Nifty 50 index. Model selection is guided by the Bayesian Information Criterion (BIC), which helped identify the most suitable ARIMA specification. The analysis revealed that double differencing provided the most stable and accurate model. The resulting forecast predicts a decline in Tata Motors' stock price in 2024, followed by a gradual upward trend in the years ahead.

**Technical Skills and Tools**:
This project demonstrates strong capabilities in time series forecasting, data transformation, model evaluation, and economic trend analysis. Specific skills include ARIMA modeling, stationarity testing, model selection using BIC, and time series visualization. The tools employed for this analysis include Stata for statistical modeling and forecasting, Excel for data preprocessing and aggregation, and Microsoft Word for academic documentation and report writing.

**Key Findings**:
The ARIMA model incorporating double differencing offered the best fit for forecasting Tata Motors’ stock price, based on model selection criteria. The forecast indicates a short-term decline in 2024, followed by a recovery and consistent upward trajectory in subsequent years. The study also reinforces the significance of macroeconomic indicators—such as the Nifty 50 index—as effective predictors of individual stock performance.

**Files**:
- [Forecasting Code](../assets/Time%20series%20econometrics/Forecasting%20code.txt)
- [Stata Do File](../assets/Time%20series%20econometrics/Forecasting%20do%20file.do)
- [Research Paper (PDF)](../assets/Time%20series%20econometrics/Forecasting.stock%20market.pdf)
- [Dataset](../assets/Time%20series%20econometrics/Tata_motors_Nifty50.xlsx)



---

## 3. Data Management – SQL Simulation for Subscription Business

**Description**: Simulates a subscription-based magazine company (BABA) by designing a schema, generating synthetic data, and extracting insights using SQL.

**Files**:
- [Faker Python Code](../assets/Data_Management/Code/Fake_data_code.py)
- [Project Report (PDF)](../assets/Data_Management/Report/Data_Management_Report.pdf)

**Skills**: SQL database design, synthetic data generation, analytics  
**Tools**: Python (pandas, faker), SQL, PowerPoint  
**Key Insights**: Demonstrates the utility of database simulation in identifying trends in customer behavior, revenue, and engagement, despite synthetic constraints.

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
