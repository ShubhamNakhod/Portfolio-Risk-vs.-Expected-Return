# Efficient Frontier: Portfolio Risk vs. Expected Return

## Project Overview
This project simulates the Efficient Frontier for portfolio optimization by analyzing the trade-off between risk (volatility) and expected return using real stock market data. 
It fetches historical prices from Yahoo Finance, computes expected returns and covariance, and simulates portfolio allocations to visualize risk-return relationships.

## Features
- Fetches real stock data for multiple assets from Yahoo Finance.
- Computes expected returns and covariance matrix from historical returns.
- Simulates 10,000 portfolio allocations with random weight distributions.
- Plots the Efficient Frontier showing risk vs. expected return.
- Incorporates Sharpe Ratio as a color scale for portfolio efficiency.

## Installation & Requirements
To run this project, install the required Python libraries:

```bash
pip install numpy pandas matplotlib yfinance
```

## How It Works
1. Fetch real stock data from Yahoo Finance.
2. Compute daily percentage returns.
3. Compute expected returns and covariance matrix.
4. Generate 10,000 random portfolio weight allocations.
5. Compute expected portfolio returns and standard deviation (risk).
6. Plot the Efficient Frontier with a Sharpe Ratio color scale.

## Applications
- **Portfolio Optimization** - Helps in selecting the optimal mix of assets to maximize return for a given level of risk.
- **Risk Management** - Assists in constructing diversified portfolios to minimize variance.
- **Quantitative Trading** - Used in algorithmic trading strategies that balance risk and return.
