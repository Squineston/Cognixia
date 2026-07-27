from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import CreateAccountRequest, AccountResponse, AmountRequest, TransactionResponse
from app.services import AccountService

router = APIRouter(prefix="/api/accounts", tags=["Accounts"])

@router.post("", response_model=AccountResponse)
def create_account(req: CreateAccountRequest, db: Session = Depends(get_db)):
    return AccountService.create_account(db, req.name, req.email, req.accountType)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    return AccountService.get_account(db, account_id)

@router.post("/{account_id}/deposit")
def deposit(account_id: int, req: AmountRequest, db: Session = Depends(get_db)):
    return AccountService.deposit(db, account_id, req.amount)

@router.post("/{account_id}/withdraw")
def withdraw(account_id: int, req: AmountRequest, db: Session = Depends(get_db)):
    return AccountService.withdraw(db, account_id, req.amount)

@router.get("/{account_id}/transactions", response_model=List[TransactionResponse])
def get_transactions(account_id: int, db: Session = Depends(get_db)):
    return AccountService.get_transactions(db, account_id)