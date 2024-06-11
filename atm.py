#program to display atm transaction

class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Current Balance:", self.balance)


def main():
    atm = ATM()
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.display_balance()
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
