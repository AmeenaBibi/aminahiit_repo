import random
acc_no = ''.join(str(random.randint(0, 9)) for i in range(10))
print("Generated account number: ", acc_no)

import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

choice = input("Do you want to set a password or generate it randomly? (set/generate): ")

if choice.lower() == "set":
    password = input("Enter your desired password: ")
elif choice.lower() == "generate":
    password_length = int(input("Enter the desired password length: "))
    password = generate_random_password(password_length)
else:
    print("Invalid choice. Please choose 'set' or 'generate'.")

if password:
    print("Your password is:", password)





