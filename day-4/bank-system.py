import json
def get_bank_account_by_account_number():
    account_number = input("Enter the account number:- ")
    is_exist = False
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
                is_exist = True
                break
            else:
                is_exist = False
        if is_exist:
            return BankAccount(line.get("account_number"), line.get("account_holder_name"), line.get("balance"))
        else:
            return None

def load_account_data():
    try:
        with open("accounts.json", "r") as file:
            lines = json.load(file)
    except FileNotFoundError:
        lines = []
    except json.JSONDecodeError:
        lines = []
    return lines

def save_account_data(lines):
    with open("accounts.json", "w") as file:
        json.dump(lines, file)

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def account_create(self):
        try:
            account_exist = False
            lines = load_account_data()
            for line in lines:
                if self.account_number == line.get("account_number"):
                    print("Account exist with this number")
                    account_exist = True
                    break
            if not account_exist:
                bank_account = {"account_number": self.account_number, "account_holder_name": self.account_holder_name, "balance": self.balance}
                lines.append(bank_account)
                save_account_data(lines)
            else:
                save_account_data(lines)

        except ValueError as error:
            print(error)

    def withdraw(self, balance):
        lines = load_account_data()
        if not lines:
            print("Account not found")
        account_list = []
        updatable = False
        for line in lines:
            if self.account_number == line.get("account_number"):
                if line["balance"] < balance:
                    print("Insufficient Balance")
                else:
                    line["balance"] =  line["balance"] - balance
                    self.balance = line["balance"]
                    account_list.append(line)
                    updatable = True
            else:
                account_list.append(line)
        if updatable:
            save_account_data(account_list)

    def check_balance(self):
        print("Your Current balance is ", self.balance)

    def check_details(self):
        print("Account Holder Name:- ",self.account_holder_name)
        print("Account Number:- ",self.account_number)
        print("Bank Balance:- ", self.balance)

    def deposit(self, balance):
        lines = load_account_data()
        if lines == []:
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
                save_account_data(account_list)

def main():
    print("\n--- BANK MENU ---")
    print("1. Create account:- ")
    print("2. Withdraw:- ")
    print("3. Check Balance:- ")
    print("4. Check Bank Details:- ")
    print("5. Deposit:- ")
    print("6. For exit press any key")
    while True:
        try:
            opt = int(input("Enter your choice:- "))
            if opt == 1:
                name = input("Enter the account holder name:- ")
                account_number = input("Enter the account number:- ")
                balance = int(input("Enter the balance:- "))
                BankAccount(account_number, name, balance).account_create()
            elif opt == 2:
                account = get_bank_account_by_account_number()
                balance = int(input("Enter the balance:- "))
                if account.balance < balance:
                    print("Insufficient Balance")
                else:
                    account.withdraw(balance)
            elif opt == 3:
                account = get_bank_account_by_account_number()
                if account != None:
                    account.check_balance()
                else:
                    print("Account not found for given account number")
            elif opt == 4:
                account = get_bank_account_by_account_number()
                if account != None:
                    account.check_details()
                else:
                    print("Account not found for given account number")
            elif opt == 5:
                account = get_bank_account_by_account_number()
                if account != None:
                    balance = int(input("Enter the balance:- "))
                    if balance <= 0:
                        print("Invalid Amount")
                    else:
                        account.deposit(balance)
                else:
                    print("Account not found for given account number")
            else:
                print("Thank you")
                break
        except Exception as error:
            print(error)
            break

if __name__ == "__main__":
    main()