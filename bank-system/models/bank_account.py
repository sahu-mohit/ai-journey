from utils.file_handler import FileHandler as f

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_type = account_type

    def account_create(self):
        try:
            account_exist = False
            lines = f.load_account_data()
            for line in lines:
                if self.account_number == line.get("account_number"):
                    print("Account exist with this number")
                    account_exist = True
                    break
            if not account_exist:
                bank_account = {"account_number": self.account_number, "account_holder_name": self.account_holder_name, "balance": self.balance, "account_type": self.account_type}
                lines.append(bank_account)
                f.save_account_data(lines)
            else:
                f.save_account_data(lines)

        except ValueError as error:
            print(error)

    def check_balance(self):
        print("Your Current balance is ", self.balance)

    def check_details(self):
        print("Account Holder Name:- ",self.account_holder_name)
        print("Account Number:- ",self.account_number)
        print("Account Type:- ", self.account_type)
        print("Bank Balance:- ", self.balance)

    def deposit(self, balance):
        lines = f.load_account_data()
        if not lines:
            print("Account not found")
        account_list = []
        updatable = False
        for line in lines:
            if self.account_number == line.get("account_number"):
                if balance <= 0:
                    print("Invalid Amount")
                else:
                    line["balance"] =  line["balance"] + balance
                    self.balance = line["balance"]
                    account_list.append(line)
                    updatable = True
            else:
                account_list.append(line)
        if updatable:
                f.save_account_data(account_list)
