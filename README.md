# Energy Data Engineering Projects

This repository contains two projects demonstrating data engineering and analytics skills relevant to the energy trading and operations sector.

---

## Project 1: Energy Market Data ETL Pipeline

An automated ETL pipeline that extracts monthly U.S. electric power operational data from the [EIA API](https://www.eia.gov/opendata/), transforms and validates it, and loads it into a SQL database for analysis and dashboards.

**Stack:** Python, SQL, Azure/Microsoft Fabric, Power BI

**Features:**
- Extracts >5,000 records from EIA API
- Cleans and reshapes JSON → DataFrame → SQL
- Derived metrics: cost per MWh, emission intensity, efficiency
- Validation checks: missing values, schema consistency
- Dashboard: trends in generation, costs, and emissions

---

## Project 2: Energy Price Forecasting

A forecasting model that predicts electricity costs and consumption trends using ARIMA and Prophet models, based on the cleaned dataset from Project 1.

**Stack:** Python, Jupyter, Prophet, ARIMA

**Features:**
- Time-series preprocessing
- Forecasting with ARIMA & Prophet
- Accuracy comparison (RMSE, MAPE)
- Forecast plots saved to /visuals

---

## Author
Kwabala Ndautu  
📧 ndautukwabala@gmail.com | 📍 Lusaka, Zambia  
🔗 [LinkedIn](https://www.linkedin.com/in/kwabalandautu)
