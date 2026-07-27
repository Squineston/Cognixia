import sys

users = {}
accounts = {}
transactions = {}

account_id_counter = 1
txn_id_counter = 1

def create_account():
    global account_id_counter
    print("\n--- Create Account ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    acc_type = input("Enter Account Type (SAVINGS/CHECKING): ").strip().upper()

    user_id = len(users) + 1
    users[user_id] = {"name": name, "email": email}

    acc_id = account_id_counter
    accounts[acc_id] = {
        "user_id": user_id,
        "name": name,
        "type": acc_type,
        "balance": 0.0
    }
    transactions[acc_id] = []
    account_id_counter += 1

    print(f"Success! Account Created. Your Account ID is: {acc_id}\n")

def view_account():
    print("\n--- View Account Details ---")
    try:
        acc_id = int(input("Enter Account ID: "))
        if acc_id not in accounts:
            print("Account not found!\n")
            return
        
        acc = accounts[acc_id]
        print(f"Account ID: {acc_id}")
        print(f"User Name:  {acc['name']}")
        print(f"Type:       {acc['type']}")
        print(f"Balance:    ${acc['balance']:.2f}\n")
    except ValueError:
        print("Invalid input! Please enter a numeric Account ID.\n")

def deposit():
    global txn_id_counter
    print("\n--- Deposit Money ---")
    try:
        acc_id = int(input("Enter Account ID: "))
        if acc_id not in accounts:
            print("Account not found!\n")
            return

        amount = float(input("Enter Deposit Amount: "))
        if amount <= 0:
            print("Deposit amount must be positive!\n")
            return

        accounts[acc_id]["balance"] += amount
        transactions[acc_id].append({
            "txn_id": txn_id_counter,
            "type": "DEPOSIT",
            "amount": amount
        })
        txn_id_counter += 1
        print(f"Successfully deposited ${amount:.2f}. New Balance: ${accounts[acc_id]['balance']:.2f}\n")
    except ValueError:
        print("Invalid input!\n")

def withdraw():
    global txn_id_counter
    print("\n--- Withdraw Money ---")
    try:
        acc_id = int(input("Enter Account ID: "))
        if acc_id not in accounts:
            print("Account not found!\n")
            return

        amount = float(input("Enter Withdrawal Amount: "))
        if amount <= 0:
            print("Withdrawal amount must be positive!\n")
            return

        if accounts[acc_id]["balance"] < amount:
            print("Insufficient balance!\n")
            return

        accounts[acc_id]["balance"] -= amount
        transactions[acc_id].append({
            "txn_id": txn_id_counter,
            "type": "WITHDRAWAL",
            "amount": amount
        })
        txn_id_counter += 1
        print(f"Successfully withdrew ${amount:.2f}. New Balance: ${accounts[acc_id]['balance']:.2f}\n")
    except ValueError:
        print("Invalid input!\n")

def view_transactions():
    print("\n--- Transaction History ---")
    try:
        acc_id = int(input("Enter Account ID: "))
        if acc_id not in accounts:
            print("Account not found!\n")
            return

        txns = transactions.get(acc_id, [])
        if not txns:
            print("No transactions found.\n")
            return

        print(f"{'Txn ID':<10}{'Type':<15}{'Amount':<10}")
        print("-" * 35)
        for t in txns:
            print(f"{t['txn_id']:<10}{t['type']:<15}${t['amount']:<10.2f}")
        print()
    except ValueError:
        print("Invalid input!\n")

def main():
    while True:
        print("=== SIMPLE BANK APPLICATION ===")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            print("Thank you for using Simple Bank!")
            sys.exit()
        else:
            print("Invalid selection. Try again.\n")

if __name__ == "__main__":
    main()