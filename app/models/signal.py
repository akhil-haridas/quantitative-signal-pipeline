from pydantic import BaseModel, Field

class Signal(BaseModel):
    symbol: str
    side: str
    qty: float = Field(gt=0)
    price: float = Field(gt=0)