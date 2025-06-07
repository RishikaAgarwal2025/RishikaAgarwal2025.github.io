---
layout: archive
title: "Academic Projects"
permalink: /projects/
author_profile: false
---


Below is a curated list of academic and applied projects, covering data analytics, forecasting, optimization, simulation modeling, A/B testing, and business analysis. Each project includes code, datasets, reports, and insights gained.

---
## 1. Forecasting Tata Motors' Stock Price using Nifty 50

**Tools used**: Stata, Excel

This project involved building a time series forecasting model to analyze the relationship between Tata Motors’ stock price and the Nifty 50 index. I performed stationarity testing, applied double differencing, and selected the optimal ARIMA model using the Bayesian Information Criterion (BIC). The model, based on annual average closing prices from 2012 to 2022, forecasts a temporary decline in 2024 followed by a long-term upward trend. This work highlights my ability to use statistical modeling techniques to understand macroeconomic influences on firm-level performance.

**Files**:
- [Forecasting Code](../assets/Time%20series%20econometrics/Forecasting%20code.txt)
- [Research Paper (PDF)](../assets/Time%20series%20econometrics/Forecasting_stock_market.pdf)
- [Dataset](../assets/Time%20series%20econometrics/Tata_motors_Nifty50.xlsx)

---

## 2. Data Management – SQL Simulation for Subscription Business

**Tools used**: Python (faker, pandas), SQL

To simulate real-world business scenarios, I designed a relational database for a fictional magazine subscription company. The schema captured customer demographics, subscriptions, payments, and engagement data. Using Python, realistic synthetic data was generated to simulate rental patterns, while SQL was used to perform complex queries reflecting real business scenarios.  Insights derived include churn rates, revenue trends, and customer lifetime value across different regions and product tiers. This project combines data engineering and business analytics to derive actionable insights in data-constrained environments.

**Files**: 
- [Faker Python Code](/assets/Data%20Management/Code/Fake%20data%20code.py)
- [Project Report (PDF)](/assets/Data%20Management/Report/Data%20Management_Report.pdf)

---

## 3. Evaluating a Loan Review Model via A/B Testing

**Tools used**: R

This project evaluated a new loan review model using an A/B testing framework within a consumer lending firm. By comparing error rates (Type I and II) between treatment (new model) and control (existing system) groups, the analysis showed that the new model significantly reduced both false approvals and rejections. The project also identifies areas for improving the experimental design like better group balancing and increasing sample size. It demonstrates practical use of hypothesis testing, experimental data analysis, and clear interpretation of results for business impact.

**Files**: 
- [HTML Output](/assets/Treatment%20control%20testing/Code/Treatment%20control%20testing.html)
- [Report (PDF)](/assets/Treatment%20control%20testing/Report/Treatment%20Control%20Testing%20Report.pdf)
- [Dataset](/assets/Treatment%20control%20testing/Data/Data.csv)

---

## 4. Pricing Analytics for BuildMax Rentals

**Tools used**: Python (Pyomo), MS PowerPoint  

This project focuses on revenue management and dynamic pricing for BuildMax Rentals to improve equipment pricing and fleet allocation. Using historical rental data and a linear programming model built in Python, we optimized pricing strategies to maximize revenue. The approach considers factors like rental duration, sector-specific demand, and maintenance schedules. By addressing pricing gaps and demand variability, the solution helps BuildMax make smarter, data-driven decisions, stay competitive, and enhance overall business performance.

**Files**:
- [Python Code](https://github.com/RishikaAgarwal2025/RishikaAgarwal2025.github.io/blob/master/assets/Pricing%20Analytics/Code.py)
- [Report (PDF)](https://github.com/RishikaAgarwal2025/RishikaAgarwal2025.github.io/blob/master/assets/Pricing%20Analytics/Report.pdf)
- [Dataset](https://github.com/RishikaAgarwal2025/RishikaAgarwal2025.github.io/blob/master/assets/Pricing%20Analytics/BuildMax_Rentals_Dataset_Updated.xlsx)

---

## 5. Analytics in Practice – Brazilian E-commerce Dataset

**Tools used**: Python, PowerPoint  

This project aimed to build a predictive model for Nile, a South American eCommerce platform, to identify customers likely to leave positive reviews. Using Python and machine learning techniques such as Logistic Regression, SVM, XGBoost, and Gradient Boosting, customer and order data were analyzed to support targeted engagement strategies. After evaluating multiple models, the Gradient Boosting model was selected for its performance, though issues with underprediction and underfitting were identified. Recommendations included improving data balance and expanding feature sets to enhance predictive accuracy. Visual insights and results were presented using PowerPoint. This project highlights practical skills in data cleaning, analysis, model building, and performance tuning, with the goal of improving customer retention and platform reputation.

**Files**:
- [Python Code](../assets/Analysis%20in%20Practice/AIP_code.ipynb)
- [Report (PDF)](../assets/Analysis%20in%20Practice/AIP_report.pdf)
- [Presentation](../assets/Analysis%20in%20Practice/AIP_presentation.pdf)
- [Dataset](../assets/Analysis%20in%20Practice/brazilian-ecommerce-dataset)

---

## 6. Business Statistics

**Assignment 1: York Footfall Analysis** 

**Tool used**: R 

This assignment involved analyzing foot traffic data from three prominent streets in York to identify the most suitable location for setting up a retail stall. The analysis included data cleaning, exploratory analysis, and visual comparisons of footfall patterns across the locations. The results indicated that one street showed the most consistent and stable foot traffic, making it the most reliable option for a business stall. In contrast, the other two streets displayed greater variability, suggesting they may be less predictable for business planning. The analysis applied statistical techniques and visualizations in R to support evidence-based decision-making related to location selection.

**Files**:
- [York Footfall Dataset](../assets/Business%20Statistics/Assignment%201/York_Footfall_data.csv)
- [Business Statistics Assignment 1 Code](../assets/Business%20Statistics/Assignment%201/Code/Business%20Statistic_Assignment1.rmd)

**Assignment 2: Analysis of Cardiovascular Disease and Customer Satisfaction**

**Tool used**: R 

This assignment analyzed two datasets to understand factors influencing cardiovascular disease (CVD) prevalence in England and customer satisfaction in retail stores.

The CVD analysis found that poverty, smoking, overweight prevalence, and wellbeing significantly affect disease rates. Notably, poverty showed a negative association with CVD, meaning higher poverty corresponded to lower disease rates, while smoking, overweight, and lower wellbeing were linked to higher CVD prevalence. Other factors may also play a role and need further investigation.

The customer satisfaction study showed that staff satisfaction and delivery time strongly impact overall satisfaction. Medium SES stores saw the greatest positive effect. These results highlight the importance of improving delivery efficiency and employee satisfaction, especially in Medium and High SES areas.

Both analyses used R for data cleaning, analysis, and visualization, offering useful insights for public health and retail management strategies.

**Files**:
- [Business Statistics Assignment_2 Code](../assets/Business%20Statistics/Assignment%202/Code/Code_Assignment.Rmd)
- [Customer Satisfaction Dataset](../assets/Business%20Statistics/Assignment%202/Dataset/cust_satisfaction.csv)
- [Cardiovascular Disease Dataset](../assets/Business%20Statistics/Assignment%202/Dataset/Cardio_Vascular_Disease.csv)

---

## 7. Understanding Business for Analysts – Case Study on MyProtein

**Tools used**: MS word, Latex, MS PowerPoint

**Description**: Uses the DELTA framework to assess MyProtein’s data strategy. Includes stakeholder analysis, risk planning, and AI-driven personalization proposals.

**Files**:
- [Report (PDF)](../assets/Understanding%20Business%20for%20Analysts/Repoort%20-%20UBFA.pdf)

**Skills**: Strategic analysis, stakeholder evaluation, business interpretation  
**Tools**: MS Word, MS PowerPoint  
**Key Insights**: MyProtein shows strong data use but needs better scalability. Recommends small-scale AI pilot programs with feedback loops to reduce bias and enhance customer engagement.
