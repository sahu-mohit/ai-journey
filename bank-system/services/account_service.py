from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
import json
class AccountService:
    def get_bank_account_by_account_number():
        account_number = input("Enter the account number:- ")
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
