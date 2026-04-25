from fastapi import FastAPI
from app.api import webhook, report

app = FastAPI(title="Quant Signal Pipeline")

app.include_router(webhook.router)
app.include_router(report.router)