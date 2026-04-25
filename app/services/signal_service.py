from datetime import datetime
import json
from pathlib import Path

seen = set()

def process_signal(signal):
    key = f"{signal.symbol}-{signal.side}-{signal.price}"

    if key in seen:
        raise ValueError("Duplicate signal")

    seen.add(key)

    Path("data").mkdir(exist_ok=True)

    with open("data/signals.log", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "signal": signal.dict()
        }) + "\n")