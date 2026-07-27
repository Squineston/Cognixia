from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import UserRepository, AccountRepository, TransactionRepository

class AccountService:
    @staticmethod
    def create_account(db: Session, name: str, email: str, account_type: str):
        user = UserRepository.get_by_email(db, email)
        if not user:
            user = UserRepository.create_user(db, name, email)
        
        account = AccountRepository.create_account(db, user.user_id, account_type)
        return {
            "accountId": account.account_id,
            "userName": user.name,
            "balance": float(account.balance)
        }

    @staticmethod
    def get_account(db: Session, account_id: int):
        account = AccountRepository.get_by_id(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return {
            "accountId": account.account_id,
            "userName": account.user.name,
            "balance": float(account.balance)
        }

    @staticmethod
    def deposit(db: Session, account_id: int, amount: float):
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Deposit amount must be positive")
        
        account = AccountRepository.get_by_id(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        new_balance = float(account.balance) + amount
        AccountRepository.update_balance(db, account, new_balance)
        TransactionRepository.create_transaction(db, account_id, "DEPOSIT", amount)

        return {"message": "Deposit successful", "balance": new_balance}

    @staticmethod
    def withdraw(db: Session, account_id: int, amount: float):
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Withdrawal amount must be positive")

        account = AccountRepository.get_by_id(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        if float(account.balance) < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")

        new_balance = float(account.balance) - amount
        AccountRepository.update_balance(db, account, new_balance)
        TransactionRepository.create_transaction(db, account_id, "WITHDRAWAL", amount)

        return {"message": "Withdrawal successful", "balance": new_balance}

    @staticmethod
    def get_transactions(db: Session, account_id: int):
        account = AccountRepository.get_by_id(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        transactions = TransactionRepository.get_by_account_id(db, account_id)
        return [
            {
                "txn_id": t.txn_id,
                "type": t.txn_type,
                "amount": float(t.amount),
                "date": t.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            for t in transactions
        ]