import argparse
from app.services.backtest_service import run_backtest
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL")
    args = parser.parse_args()

    result = run_backtest(args.symbol)

    output_path = Path("data") / "backtest_results.json"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print(f"Backtest completed for {args.symbol}")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()