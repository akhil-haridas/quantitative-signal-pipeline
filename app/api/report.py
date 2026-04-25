from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/report")
def report():
    try:
        with open("data/backtest_results.json") as f:
            return json.load(f)
    except:
        return {"error": "No data"}