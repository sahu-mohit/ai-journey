from utils.file_handler import FileHandler as f
from models.bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, account_type):
        super().__init__(account_number, account_holder_name, balance, account_type)

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
