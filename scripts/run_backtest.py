from app.services.backtest_service import run_backtest
import json
from pathlib import Path


def main():
    symbol = "AAPL"  # configurable later

    result = run_backtest(symbol)

    output_path = Path("data") / "backtest_results.json"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print("Backtest completed successfully")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()