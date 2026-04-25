from datetime import datetime
import json
from pathlib import Path
import uuid

seen = set()


def process_signal(signal):
    signal_id = str(uuid.uuid4())

    key = f"{signal.symbol}-{signal.side}-{signal.price}"

    if key in seen:
        raise ValueError("Duplicate signal")

    seen.add(key)

    log_entry = {
        "id": signal_id,
        "timestamp": datetime.utcnow().isoformat(),
        "symbol": signal.symbol,
        "side": signal.side,
        "qty": signal.qty,
        "price": signal.price
    }

    Path("data").mkdir(exist_ok=True)

    with open("data/signals.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return log_entry