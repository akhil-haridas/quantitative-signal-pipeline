from fastapi import APIRouter, HTTPException
from app.models.signal import Signal
from app.services.signal_service import process_signal
from app.services.execution_service import execute_signal

router = APIRouter()

@router.post("/webhook")
def webhook(signal: Signal):
    try:
        process_signal(signal)
        execute_signal(signal)
        return {"status": "ok"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))