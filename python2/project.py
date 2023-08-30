# Banking Application
acctNo = 0
customerName = ""
bCode = ""
mobile = 0
balance = 0

def CreateAccount():
    global acctNo
    global customerName
    global bCode
    global mobile
    global balance
    global setPassword

    customerName = input("Enter name: ")
    bCode = input("Enter branch code: ")
    mobile = int(input("Enter mobile number: "))
    balance = int(input("Enter current balance: "))

    import random
    acctNo = ''.join(str(random.randint(0, 9)) for i in range(10))
    print("Generating account number.....")
    print("Your new account number is: ", acctNo)

    import random
    import string
    def setPassword(length=12):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    choice = input("Do you want to set a password or generate it randomly? (set/generate): ")

    if choice == "set":
        password = input("Set a password: ")
    elif choice == "generate":
        password_length = int(input("Enter the desired length of password: "))
        password = setPassword(password_length)
    else:
        print("Invalid choice. Please select from the options provided.")
    if password:
        print("Your password is: ", password)
print("Welcome to Fanas Bank:)\nWhat do you want to do?")

def showAccountDetails():
    print("Bank Name: Fanas Bank")
    print("Account Number: ", acctNo)
    print("Customer Name: ", customerName)
    print("Branch Code: ", bCode)
    print("Mobile Number: ", mobile)
    print("Thank you for banking with us, see you next time!")


def deposit(amount):
    global balance
    balance = balance + amount
    checkbalance()

def withdraw(amount):
    global balance
    balance = balance - amount
    checkbalance()

def checkbalance():
    print("Current Balance: ", balance)

#_Main_#
ch = 'x'
while ch == 'x':
    print("1. Create account:\n2. Deposit:\n3. Withdraw:\n4. Check balance:\n5. Exit")
    choice = int(input("Select any option: "))
    if choice == 1:
        CreateAccount()
    elif choice == 2:
        amnt = int(input("Enter amount to deposit: "))
        deposit(amnt)
    elif choice == 3:
        amnt = int(input("Enter amount to withdraw: "))
        withdraw(amnt)
    elif choice == 4:
        checkbalance()
    elif choice == 5:
        break
    else:
        print("Please select a valid choice")
    print("do you want to continue... press x")
    ch = input()

showAccountDetails()