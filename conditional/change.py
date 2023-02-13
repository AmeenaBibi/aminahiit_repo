debt = int(input("Where is my change: "))

if debt != 3000:
        print("Oshey baddest")
elif debt > 3000:
        print(f"This is too much, comot {debt-3000}")
else:
    print(f"This money no reach, give me {3000-debt}")