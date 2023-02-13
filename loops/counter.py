sentence = input("What are you saying: ")
counter = 0

for letter in sentence:
    if letter != " ":
        counter += 1

print(counter)