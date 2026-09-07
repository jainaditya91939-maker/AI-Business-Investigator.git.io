from pydantic import BaseModel, Field
from datetime import date
from typing import Literal
from decimal import Decimal


class SupplierCreate(BaseModel):
    name: str
    phone: str | None = None
    address: str | None = None


class TransactionCreate(BaseModel):
    supplier_id: int

    transaction_type: Literal[
        "PURCHASE",
        "PAYMENT",
        "RETURN",
        "CREDIT_NOTE"
    ]

    amount: Decimal = Field(
    gt=0,
    max_digits=12,
    decimal_places=2
)

    transaction_date: date
    reference_number: str | None = None
    notes: str | None = None