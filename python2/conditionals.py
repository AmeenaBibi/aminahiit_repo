country = input("Enter country: ").lower().upper()
if country == "Nigeria".lower().upper():
    age = int(input("Enter age: "))
    if age >= 18:
        state = input("Enter state: ")
        print("You're good to go.")
    else:
        print("You are not eligible to vote due to age.")
else:
    print("You are not eligible to vote from this country")