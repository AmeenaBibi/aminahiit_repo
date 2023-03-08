class BankAccount:
    def __init__(self, name, type, acctNumber, balance = 0):
        self.acctName = name
        self.acctType = type
        self.acctNumber = acctNumber
        self.balance = balance
        self.transactionHistory = []

    def deposite_money(self, amount):
        amount = int(amount)
        self.balance += amount
        self.transactionHistory.append(('Credit', amount))
        print('Successful')

    def withdraw_money(self, amount):
        amount = int(amount)
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            self.transactionHistory.append(('Debit', amount))
            print('Successful')

    def check_balance(self):
        print(self.balance)

    def transaction_history(self):
        for transact in self.transactionHistory:
            print(transact)

def main():
    bank_users = []

    while True:
        print()
        print()
        print('Welcome to my bank')
        print('What would you like to do?')
        print('1. Create an account')
        print('2. Deposite money')
        print('3. Withdraw money')
        print('4. Check balance')
        print('5. Check transaction history')
        print('6. Exit')
        choice = input("What's your choice?: ")
        if choice == '1':
            name = input('Enter your name: ')
            acctType = input('Enter your account type (savings/current): ')
            acctNumber = int(input('Enter your account number: '))
            newAcct = BankAccount(name, acctType, acctNumber)
            bank_users.append(newAcct)
        elif choice == '2':
            acct = input('Please enter your account number: ')
            amount = input('Enter amount you want to deposite: ')
            if len(bank_users) >= 1:
                for user in bank_users:
                    if user.acctNumber ==int(acct):
                        user.deposite_money(amount)
                        break
                    else:
                        print('No')
                else:
                    print('Could not find the accout')
            else:
                print('No bank user')
        elif choice == '3':
            acct = input('Please enter your account numbeer: ')
            amount = input('Enter amount you want to withdraw: ')
            if len(bank_users) >= 1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        user.withdraw_money(amount)
                        break
                    else:
                        print('Could not find account')
                else:
                    print('No bank user')
        elif choice == '4':
            acct = input('Enter you account number: ')
            if len(bank_users) >= 1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        print('Balance: ')
                        user.check_balance()
                        break
                    else:
                        print('Could not find account')
                else:
                    print('No bank user')
        elif choice == '5':
            acct = input('Enter your account number: ')
            if len(bank_users) >= 1:
                for user in bank_users:
                    if user.acctNumber == int(acct):
                        print('Transaction history: ')
                        user.transaction_history()
                        break
                    else:
                        print('Could not find account')
            else:
                print('No bank user')
        elif choice == '6':
            break


main()