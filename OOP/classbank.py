def main():
    while True:
        print("""
                press 1 to create new account
                press 2 to deposit to the account
                press 3 to withdraw from the account
                press 4 to check current balance
                press 5 to display transaction history
                press 6 to exit
                """)
        resp = input('Select an option: ')
        if resp == '1':
            create_acc()
            continue
        if resp == '2':
            deposit_acc()
            continue
        if resp == '3':
            withdraw_acc()
            continue
        if resp == '4':
            check_bal()
            continue
        if resp == '5':
            disp_history()
            continue
        if resp == '6':
            break
        else:
            print('Not a valid choice')
            continue


class BankAccount:
    def __init__(self, number, holder_name, type, balance):
        self.number = number
        self.holder_name = holder_name
        self.type = type
        self.balance = balance
 
acc = BankAccount('any', 'any', 'savings/checking', 5000)


def create_acc():
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')
    account = {'name': name, 'phone': phone, 'email': email}
    print(account)

def deposit_acc():
    deposite = int(input('Amount to be deposited: '))
    amount = acc.balance + deposite
    print(f'Current balance is {amount}')

def withdraw_acc():
    withdraw = int(input('Amount to be withdrawn: '))
    amount = acc.balance - withdraw
    print(f'{amount}')

# def check_bal():

# def disp_history():

main()
