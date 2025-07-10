class bank_account:
    def __init__(self, username, password, balance):
        self.username = username
        self.balance = float(balance)
        self.password = password

    def authenticate(self, input_username, input_password):
        return self.username == input_username and self.password == input_password

    def deposit(self, amount):
        try:
            amount = float(amount)  
            if amount <= 0:
                print(" Deposit amount must be positive.")
            else:
                self.balance += amount
                print(f" Deposited: {amount:.2f} PKR")
        except ValueError:
            print(" Invalid amount. Please enter a number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print(" Withdrawal amount must be positive.")
            elif amount > self.balance:
                print(" Insufficient balance.")
            else:
                self.balance -= amount
                print(f" Withdrawn: {amount:.2f} PKR")
        except ValueError:
            print(" Invalid amount. Please enter a number.") 

    def check_balance(self):
        print(f" Current Balance: {self.balance:.2f} PKR")

    def menu(self):  
        while True:
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Enter choice (1-4): ")

            if choice == "1":
                amount = input("Enter amount to deposit: ")
                self.deposit(amount)
            elif choice == "2":
                amount = input("Enter amount to withdraw: ")
                self.withdraw(amount)
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print(" Exiting. Thank you for using our service.")
                break
            else:
                print(" Invalid choice. Please select 1 to 4.")

if __name__ == "__main__":
    accounts = {
        "Saqlain": bank_account("Saqlain", "123", 1000),
        "Ali": bank_account("Ali", "456", 2000),
        "Ahmed": bank_account("Ahmed", "789", 1500)
    }

    print(" Welcome to State Bank of Pakistan")
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    if input_username in accounts:
        user_name = accounts[input_username]

        if user_name.authenticate(input_username, input_password):
            print("\n Login successful!\n")
            user_name.menu()
        else:
            print(" Authentication failed. Incorrect password.")
    else:
        print(" Username not found.")
