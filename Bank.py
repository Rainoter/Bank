class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.loan = 0  # Initialize loan amount for each account

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into {self.name}'s account.")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount} from {self.name}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount should be greater than zero.")

    def request_loan(self, amount):
        if amount > 0:
            self.loan += amount
            self.balance += amount
            print(f"{self.name} has taken a loan of ${amount}.")
        else:
            print("Loan amount should be greater than zero.")

    def repay_loan(self, amount):
        if amount > 0:
            if self.loan >= amount:
                self.loan -= amount
                self.balance -= amount
                print(f"{self.name} repaid ${amount} of the loan.")
            else:
                print("Loan amount to repay is more than the loan balance.")
        else:
            print("Repayment amount should be greater than zero.")

    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")
        print(f"{self.name}'s loan balance: ${self.loan}")


class BankSystem:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts

    def create_account(self, name):
        if name not in self.accounts:
            self.accounts[name] = BankAccount(name)
            print(f"Account for {name} created.")
        else:
            print("Account already exists.")

    def login(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account does not exist.")
            return None

    def add_money_to_account(self, admin_password):
        if admin_password == "rainoter":  # This is a simple admin password for demonstration
            name = input("Enter account holder's name: ")
            if name in self.accounts:
                amount = float(input("Enter amount to add: "))
                self.accounts[name].deposit(amount)
            else:
                print("Account does not exist.")
        else:
            print("Admin password incorrect.")


bank = BankSystem()

while True:
    print("\nWelcome to the Simple Bank System")
    print("1. Create Account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Request Loan")
    print("7. Repay Loan")
    print("8. Admin - Add Money to Account")
    print("9. Exit")
    choice = input("Enter choice (1-9): ")

    if choice == '1':
        name = input("Enter your name: ")
        bank.create_account(name)

    elif choice == '2':
        name = input("Enter your name: ")
        current_account = bank.login(name)
        if current_account:
            while True:
                print("\nOptions:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Request Loan")
                print("5. Repay Loan")
                print("6. Logout")
                option = input("Enter option (1-6): ")

                if option == '1':
                    amount = float(input("Enter amount to deposit: "))
                    current_account.deposit(amount)

                elif option == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    current_account.withdraw(amount)

                elif option == '3':
                    current_account.check_balance()

                elif option == '4':
                    amount = float(input("Enter loan amount: "))
                    current_account.request_loan(amount)

                elif option == '5':
                    amount = float(input("Enter repayment amount: "))
                    current_account.repay_loan(amount)

                elif option == '6':
                    print("Logged out.")
                    break

                else:
                    print("Invalid option. Please try again.")

    elif choice == '8':
        admin_password = input("Enter admin password: ")
        bank.add_money_to_account(admin_password)

    elif choice == '9':
        print("Exiting the bank system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
