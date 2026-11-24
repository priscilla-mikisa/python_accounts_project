class Account:
    def __init__(self):
        self.accounts_list = []   # List of account dictionaries for all accounts
        self.no_account = "Account not found."

    def add_account_owner(self, account_user_name: str, account_pin: str):
        account_number = len(self.accounts_list) + 1

        new_account = {
            "account_user_name": account_user_name,
            "account_pin": account_pin,
            "account_number": account_number,
            "balance": 0.0
        }
        self.accounts_list.append(new_account)
        print(f"Account {account_number} created for {account_user_name}")
        return new_account

    def deposit(self, account_number: int, amount: float):
        for account in self.accounts_list:
            if account["account_number"] == account_number:
                if amount > 0:
                    account["balance"] += amount
                    print(f"Deposited {amount} KES. New balance: {account['balance']}")
                return
        print( self.no_account)

    def minimum_balance_check(self, account_number: int):
        for account in self.accounts_list:
            if account["account_number"] == account_number:
                if account["balance"] < 500:
                    print(f"Insufficient account balance for Account {account_number}. "
                          "Balance must be 500 KES or more.")
                return
        print( self.no_account)

    def display_details(self, account_pin: str):
        for user in self.accounts_list:
            if user['account_pin'] == account_pin:
                print(f"User Name: {user['account_user_name']}")
                print(f"Account Number: {user['account_number']}")
                print(f"Account Pin: {user['account_pin']}")
                print(f"Balance: {user['balance']} KES")
                return
        print(f"Account not found with PIN {account_pin}.")

    def change_account_owner(self, old_account_number: int, new_user_name: str, new_account_pin: str):
        for user in self.accounts_list:
            if user['account_number'] == old_account_number:
                user['account_user_name'] = new_user_name
                user['account_pin'] = new_account_pin
                print(f"Account {old_account_number} updated successfully.")
                return
        print(self.no_account)

    def transfer_funds(self, from_account_id: int, to_account_id: int, amount: float):
        from_acc = next((acc for acc in self.accounts_list if acc["account_number"] == from_account_id), None)
        to_acc = next((acc for acc in self.accounts_list if acc["account_number"] == to_account_id), None)

        if not from_acc or not to_acc:
            print("One or both accounts not found.")
            return
        if from_acc == to_acc:
            print("Cannot transfer to the same account.")
            return
        if from_acc["balance"] < amount:
            print("Insufficient funds for transfer.")
            return

        from_acc["balance"] -= amount
        to_acc["balance"] += amount
        print(f"Transferred {amount} KES from Account {from_account_id} to Account {to_account_id}.")

    def display_all(self):
        if not self.accounts_list:
            print("No accounts yet.")
        else:
            for acc in self.accounts_list:
                print(acc)


# === Testing the improved version ===
bank = Account()

bank.add_account_owner("Miki", "234osk3")
bank.deposit(1, 500)
bank.minimum_balance_check(1)
bank.display_details("234osk3")

bank.change_account_owner(1, "Canary", "30ids")

bank.add_account_owner("Miki", "234osk3")
bank.deposit(2, 600)

bank.transfer_funds(1, 2, 100)
bank.display_all()