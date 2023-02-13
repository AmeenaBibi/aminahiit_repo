sentence1 = input("First sentence: ")
sentence2 = input("Second sentence: ")
counter1 = 0
counter2 = 0

for letter in sentence1 and sentence2:
    if letter != " ":
        counter1 += 1
        counter2 += 1

print(counter1)
print(counter2)
print(counter1 + counter2)
