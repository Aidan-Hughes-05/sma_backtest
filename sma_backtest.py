import numpy as np
import pandas as pd
import yfinance as yf

df = yf.download("AAPL", start="2018-01-01", end="2024-01-01")
print(df.head())
print(df.tail())
