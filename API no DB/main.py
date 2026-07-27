from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Bank API (In-Memory)")

# In-memory storage
users_db = {}
accounts_db = {}
transactions_db = {}

account_id_counter = 1
txn_id_counter = 1

# Pydantic Request Models
class CreateAccountRequest(BaseModel):
    name: str
    email: str
    accountType: str

class AmountRequest(BaseModel):
    amount: float

@app.post("/api/accounts")
def create_account(req: CreateAccountRequest):
    global account_id_counter
    
    user_id = len(users_db) + 1
    users_db[user_id] = {"name": req.name, "email": req.email}

    acc_id = account_id_counter
    accounts_db[acc_id] = {
        "accountId": acc_id,
        "userId": user_id,
        "userName": req.name,
        "accountType": req.accountType,
        "balance": 0.0
    }
    transactions_db[acc_id] = []
    account_id_counter += 1

    return {
        "accountId": acc_id,
        "userName": req.name,
        "balance": 0.0
    }

@app.get("/api/accounts/{account_id}")
def get_account(account_id: int):
    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")
    acc = accounts_db[account_id]
    return {
        "accountId": acc["accountId"],
        "userName": acc["userName"],
        "balance": acc["balance"]
    }

@app.post("/api/accounts/{account_id}/deposit")
def deposit(account_id: int, req: AmountRequest):
    global txn_id_counter
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")

    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")

    accounts_db[account_id]["balance"] += req.amount
    
    transactions_db[account_id].append({
        "txn_id": txn_id_counter,
        "type": "DEPOSIT",
        "amount": req.amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    txn_id_counter += 1

    return {"message": "Deposit successful", "balance": accounts_db[account_id]["balance"]}

@app.post("/api/accounts/{account_id}/withdraw")
def withdraw(account_id: int, req: AmountRequest):
    global txn_id_counter
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Withdrawal amount must be positive")

    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")

    if accounts_db[account_id]["balance"] < req.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    accounts_db[account_id]["balance"] -= req.amount

    transactions_db[account_id].append({
        "txn_id": txn_id_counter,
        "type": "WITHDRAWAL",
        "amount": req.amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    txn_id_counter += 1

    return {"message": "Withdrawal successful", "balance": accounts_db[account_id]["balance"]}

@app.get("/api/accounts/{account_id}/transactions")
def get_transactions(account_id: int):
    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")

    return transactions_db.get(account_id, [])