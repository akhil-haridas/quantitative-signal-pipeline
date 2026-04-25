import numpy as np
import pandas as pd
import yfinance as yf
import json
from pathlib import Path

def run_backtest(symbol="AAPL"):
    df = yf.download(symbol, period="6mo")

    df["ema9"] = df["Close"].ewm(span=9).mean()
    df["ema21"] = df["Close"].ewm(span=21).mean()

    df["signal"] = 0
    df.loc[df["ema9"] > df["ema21"], "signal"] = 1
    df.loc[df["ema9"] < df["ema21"], "signal"] = -1

    df["position"] = df["signal"].shift()
    df["returns"] = df["Close"].pct_change()
    df["strategy"] = df["returns"] * df["position"]

    df["strategy"] = df["returns"] * df["position"]

    strategy_std = df["strategy"].std()

    sharpe = 0
    if strategy_std and not np.isnan(strategy_std):
        sharpe = (df["strategy"].mean() / strategy_std) * np.sqrt(252)
        
    result = {
        "total_return": float(df["strategy"].sum()),
        "win_rate": float((df["strategy"] > 0).mean()),
        "max_drawdown": float(
            (df["strategy"].cumsum().cummax() - df["strategy"].cumsum()).max()
        ),
        "num_trades": int(df["position"].diff().abs().sum()),
        "sharpe_ratio": float(sharpe)  # 👈 add this
    }

    Path("data").mkdir(exist_ok=True)

    with open("data/backtest_results.json", "w") as f:
        json.dump(result, f, indent=4)

    return result