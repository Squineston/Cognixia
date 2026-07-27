from pydantic import BaseModel
from typing import List

class CreateAccountRequest(BaseModel):
    name: str
    email: str
    accountType: str

class AccountResponse(BaseModel):
    accountId: int
    userName: str
    balance: float

    class Config:
        from_attributes = True

class AmountRequest(BaseModel):
    amount: float

class TransactionResponse(BaseModel):
    txn_id: int
    type: str
    amount: float
    date: str

    class Config:
        from_attributes = True