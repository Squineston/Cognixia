from sqlalchemy.orm import Session
from app.models import User, Account, Transaction

class UserRepository:
    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, name: str, email: str):
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

class AccountRepository:
    @staticmethod
    def create_account(db: Session, user_id: int, account_type: str):
        account = Account(user_id=user_id, account_type=account_type, balance=0.00)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    @staticmethod
    def get_by_id(db: Session, account_id: int):
        return db.query(Account).filter(Account.account_id == account_id).first()

    @staticmethod
    def update_balance(db: Session, account: Account, new_balance: float):
        account.balance = new_balance
        db.commit()
        db.refresh(account)
        return account

class TransactionRepository:
    @staticmethod
    def create_transaction(db: Session, account_id: int, txn_type: str, amount: float):
        txn = Transaction(account_id=account_id, txn_type=txn_type, amount=amount)
        db.add(txn)
        db.commit()
        db.refresh(txn)
        return txn

    @staticmethod
    def get_by_account_id(db: Session, account_id: int):
        return db.query(Transaction).filter(Transaction.account_id == account_id).all()