# Efficient Frontier: Portfolio Risk vs. Expected Return

## 📌 Project Overview
This project simulates the **Efficient Frontier** for portfolio optimization by analyzing the **trade-off between risk (volatility) and expected return** using real stock market data.  
It fetches historical prices from **Yahoo Finance**, computes expected returns and covariance, and simulates portfolio allocations to visualize risk-return relationships.

---

## 🔹 Features
✔ Fetches **real stock data** for multiple assets from **Yahoo Finance**.  
✔ Computes **expected returns and covariance matrix** from historical returns.  
✔ Simulates **10,000 portfolio allocations** with random weight distributions.  
✔ Plots the **Efficient Frontier** showing **risk vs. expected return**.  
✔ Incorporates **Sharpe Ratio** as a color scale for portfolio efficiency.  

---

## 🔹 Installation & Requirements
To run this project, install the required Python libraries:

```bash
pip install numpy pandas matplotlib yfinance
