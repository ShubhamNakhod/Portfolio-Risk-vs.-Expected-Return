import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Fetching real stock data from Yahoo Finance
assets = ["AAPL", "GOOGL", "MSFT", "AMZN"]
data = yf.download(assets, start="2023-01-01", end="2024-01-01")["Close"]

# Computing daily returns
returns = data.pct_change().dropna()

# Computing expected returns and covariance matrix
expected_returns = returns.mean()
cov_matrix = returns.cov()

# Debugging: Print values to check for errors
print("Expected Returns:\n", expected_returns)
print("\nCovariance Matrix:\n", cov_matrix)

# Ensuring covariance matrix is positive semi-definite
eigenvalues = np.linalg.eigvals(cov_matrix)
print("\nEigenvalues of Covariance Matrix:", eigenvalues)

# Generating random portfolio weights
num_portfolios = 10000
weights = np.random.dirichlet(np.ones(len(assets)), num_portfolios)

# Computing portfolio returns
portfolio_returns = weights @ expected_returns.values

# Computing portfolio risk (Standard Deviation)
portfolio_variances = np.einsum('ij,jk,ik->i', weights, cov_matrix.values, weights)
portfolio_risk = np.sqrt(portfolio_variances)

# Debugging: Check for negative or zero risk values
print("\nMin Risk:", np.min(portfolio_risk), "Max Risk:", np.max(portfolio_risk))

# Ensuring risk values are positive for plotting
valid_indices = portfolio_risk > 0
portfolio_risk = portfolio_risk[valid_indices]
portfolio_returns = portfolio_returns[valid_indices]

# Plotting Efficient Frontier
plt.figure(figsize=(10, 6))
plt.scatter(portfolio_risk, portfolio_returns, c=portfolio_returns / portfolio_risk, cmap="viridis", alpha=0.5)
plt.xlabel("Risk (Standard Deviation)")
plt.ylabel("Expected Return")
plt.colorbar(label="Sharpe Ratio")
plt.title("Efficient Frontier: Portfolio Risk vs. Expected Return")
plt.show()
