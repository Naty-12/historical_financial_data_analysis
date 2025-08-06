# 📈 GMF Investments: Time Series Forecasting & Portfolio Analysis

## 🧠 Business Objective

Guide Me in Finance (GMF) Investments is a forward-thinking financial advisory firm focused on data-driven investment strategies. This project aims to support GMF’s portfolio management by leveraging historical financial data and time series forecasting techniques to:

- Identify trends and volatility in key assets,
- Prepare the data for advanced modeling (ARIMA, LSTM),
- Provide risk and return insights to inform portfolio decisions.

---

## 🗂️ Project Structure
```
📁 GMF-TimeSeries-Project/
│
├── data/ # Raw and cleaned historical financial data
├── notebooks/ # Jupyter Notebooks for analysis
│ └── task1_exploration.ipynb
├── scripts/ # Python scripts for data fetching & preprocessing
│ └── fetch_yfinance_data.py
├── plots/ # Generated plots from EDA and risk analysis
├── README.md
└── requirements.txt
```


## ✅ Task 1: Data Preprocessing & Exploration

### 📌 Goal
Clean, explore, and understand the historical financial data for three assets:  
- **Tesla (TSLA)** – High-growth, high-volatility stock  
- **Vanguard Total Bond Market ETF (BND)** – Low-risk bond ETF  
- **S&P 500 ETF (SPY)** – Broad-market index ETF

### 📈 Steps Performed

1. **Data Collection**
   - Used `yfinance` to download data from **July 1, 2015 – July 31, 2025**
   - Extracted key features: Open, High, Low, Close, Adj Close, Volume

2. **Data Cleaning**
   - Converted timestamps, set Date as index
   - Handled missing values using forward-fill
   - Ensured consistent data types

3. **Feature Engineering**
   - Calculated **daily returns**
   - Calculated **30-day rolling mean** and **rolling standard deviation**

4. **Exploratory Data Analysis**
   - Visualized price trends and return volatility
   - Identified outliers and days with extreme returns
   - Compared volatility across TSLA, BND, and SPY

5. **Stationarity Testing**
   - Applied Augmented Dickey-Fuller (ADF) test on closing prices and returns
   - Interpreted results to determine need for differencing in future modeling

6. **Risk Metrics**
   - Computed **Value at Risk (VaR)** at 95% confidence level
   - Calculated **Sharpe Ratio** for risk-adjusted returns

---

## 📊 Key Insights

- **TSLA** shows high volatility and frequent price jumps, requiring careful risk management.
- **BND** demonstrates stable performance with minimal price fluctuations.
- **SPY** provides balanced exposure, with moderate volatility.
- ADF tests indicated that price series are **non-stationary**, but daily returns are **stationary** — suitable for ARIMA/LSTM modeling.
- VaR and Sharpe Ratio give early indicators of asset-specific risk profiles.

---

## 📚 Libraries Used

- `yfinance` – Financial data API
- `pandas`, `numpy` – Data wrangling & numerical ops
- `matplotlib`, `seaborn` – Data visualization
- `statsmodels` – ADF test & time series tools

---

## 📅 Timeline

| Milestone                | Date               |
|-------------------------|--------------------|
| Project Discussion       | August 6, 2025     |
| Interim Submission       | August 10, 2025    |
| Final Submission         | August 12, 2025    |


---

## 📥 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GMF-TimeSeries-Project.git
   cd GMF-TimeSeries-Project