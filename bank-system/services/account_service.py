from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
from utils.file_handler import FileHandler as f
import json

class AccountService:
    def get_bank_account_by_account_number(account_number):
        found_account = None
        try:
            with open("accounts.json", "r") as file:
                lines = json.load(file)
        except FileNotFoundError:
            lines = []
        except json.JSONDecodeError:
            lines = []
        if not lines:
            print("Account not found")
        else:
            for line in lines:
                if account_number == line.get("account_number"):
                    found_account = line
                    break
            if found_account:
                if line.get("account_type") == "saving":
                    return SavingsAccount(line.get("account_number"), line.get("account_holder_name"), line.get("balance"), line.get("account_type"))
                elif  line.get("account_type") == "current":
                    return CurrentAccount(line.get("account_number"), line.get("account_holder_name"), line.get("balance"), line.get("account_type"))
            else:
                return None

    def withdraw(self, balance):
        balance = int(input("Enter the balance:- "))
        lines = f.load_account_data()
        if not lines:
            print("Account not found")
        account_list = []
        updatable = False
        for line in lines:
            if self.account_number == line.get("account_number"):
                if (line["balance"] - balance) < -10000:
                    print("Insufficient Balance")
                else:
                    line["balance"] =  line["balance"] - balance
                    self.balance = line["balance"]
                    account_list.append(line)
                    updatable = True
            else:
                account_list.append(line)
        if updatable:
            f.save_account_data(account_list)