import random
attempts = 0
min_value = 1
max_value = 50
max_attempts = 5
number = random.randint(min_value,max_value)

while True:
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue
    attempts += 1
    if guess == number:
        print("Congrats, you guessed right.")
        break
    elif guess < number:
        print("A little too low.")
    elif guess > number:
        print("A little too high")
    if attempts == max_attempts:
        print("No more guesses.")
        break
print("Game over!")