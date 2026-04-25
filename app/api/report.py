from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()


@router.get("/report")
def report():
    data = {}

    # Backtest
    backtest_file = Path("data/backtest_results.json")
    if backtest_file.exists():
        with open(backtest_file) as f:
            data["backtest"] = json.load(f)
    else:
        data["backtest"] = None

    # Signals
    signal_file = Path("data/signals.log")
    if signal_file.exists():
        with open(signal_file) as f:
            lines = f.readlines()

        data["signals"] = {
            "total": len(lines)
        }
    else:
        data["signals"] = {"total": 0}

    return data