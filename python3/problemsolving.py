user = input("Enter list of numbers: ").split(",")
# or user.split(", ")
listed_no = []

for i in user:
    if i.isnumeric():
        listed_no.append(int(i))
        
largest = max(user)
smallest = min(user)
print(largest)
print(smallest)