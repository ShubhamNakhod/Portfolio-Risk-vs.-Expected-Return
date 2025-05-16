**Efficient Frontier: Portfolio Risk vs. Expected Return**

This project visualizes the Efficient Frontier using real stock data and simulates thousands of portfolios to analyze the trade-off between risk and return. It calculates expected returns, portfolio variance, and the Sharpe Ratio to identify optimal investment strategies.

<pre> ```text Project Structure
├── Portfolio Risk & Expected Return.py    # Main simulation and visualization script
├── Portfolio Risk vs Expected Return.png  # Final Efficient Frontier plot
└── README.md                              # Project documentation ```</pre>

Key Concepts
- Efficient Frontier: A set of optimal portfolios offering the highest expected return for a defined level of risk.
- Sharpe Ratio: Measures risk-adjusted return; higher values indicate more efficient portfolios.
- Covariance Matrix: Captures how asset prices move relative to each other; crucial for portfolio variance.

Features
- Pulls real stock data (AAPL, GOOGL, MSFT, AMZN) from Yahoo Finance
- Computes:
  * Daily percentage returns
  * Expected returns
  * Covariance matrix
- Generates 10,000 random portfolio weight allocations
- Calculates:
  * Portfolio expected return
  * Portfolio standard deviation (risk)
  * Sharpe Ratio
- Plots the Efficient Frontier with a Sharpe Ratio heatmap

How It Works
- Data Collection
Downloads closing prices for selected tickers from 2023–2024.

- Metric Computation
Calculates expected return and risk using matrix operations.

- Portfolio Simulation
Generates weight vectors using Dirichlet distribution for 10,000 random portfolios.

- Visualization
Plots risk vs. return with Sharpe Ratio as the color scale.

Sample Output
![Portfolio Risk vs Expected Return](https://github.com/user-attachments/assets/7a46ed7a-4224-4fff-b458-9335d222c0b1)

- Installation
Install required Python libraries:
bash
pip install numpy pandas matplotlib yfinance

- Usage
Run the script:
bash
python "Portfolio Risk & Expected Return.py"

- Applications
* Portfolio Optimization: Helps identify the most efficient asset allocation.
* Risk Management: Understand the volatility-return trade-off.
* Quantitative Finance: Forms a foundation for advanced investment algorithms and financial modeling.

Notes
- Only portfolios with positive standard deviation are plotted.
- You can extend this to include:
  * Risk-free asset
  * Constraint optimization (e.g., max weight per asset)
  * Portfolio rebalancing strategies
