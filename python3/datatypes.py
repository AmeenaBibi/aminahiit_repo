# debt = int(input("Where is my change: "))

# if debt != 3000:
#         print("Oshey baddest")
#         if debt == 3000:
#                print("My change is accurate")
#                if debt > 3000:
#                      print(f"This is too much, comot {debt-3000}")
#                      if debt < 3000:
#                             print(f"This is too little, add {debt+3000}")
# else:
#     print(f"This money no reach, give me {3000-debt}")


# for i in range(0, 101):
#     print(i)

def names(list):
    name = input("Enter name: ")
    print(f"Your name is: {name}")
    for item in list:
        print(item)

list = [1, 2, 3, 4, 5]
names(list)
