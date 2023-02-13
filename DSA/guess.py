import random
guesses = []
number = random.randint(1, 100)

def guess():
    while True:
        guess = int(input("What number am i thinking of: "))
        guesses.append(guess)

        if guess == number:
            print(f"I was thinking of the number {number}")
            print(f"You guessed {guess}")
            print(f"You have guessed the number in {len(guesses)} attempts")
            break
        elif guess < number:
            print("Guess higher")
        else:
            print("Guess lower")

guess()