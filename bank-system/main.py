from models.current_account import CurrentAccount
from models.savings_account import SavingsAccount
from services.account_service import AccountService
import json
import traceback

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
                account_type = input("Enter the account type:- ")
                if account_type == "saving":
                    SavingsAccount(account_number, name, balance, account_type).account_create()
                elif account_type == "current":
                    CurrentAccount(account_number, name, balance, account_type).account_create()
                else:
                    print("Please give valid account type")
            elif opt == 2:
                account = AccountService.get_bank_account_by_account_number()
                if account != None:
                    account.withdraw(balance)
                else:
                    print("Account Not Found")
            elif opt == 3:
                account = AccountService.get_bank_account_by_account_number()
                if account != None:
                    account.check_balance()
                else:
                    print("Account not found for given account number")
            elif opt == 4:
                account = AccountService.get_bank_account_by_account_number()
                if account != None:
                    account.check_details()
                else:
                    print("Account not found for given account number")
            elif opt == 5:
                account = AccountService.get_bank_account_by_account_number()
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
            traceback.print_exc()
            break

if __name__ == "__main__":
    main()