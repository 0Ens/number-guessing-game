import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!\nTry to find my number its between 1 to 100 \nChoose a difficulty level:")

while True:
    x = input("Type 'easy' or 'hard': ").lower()
    if x == 'easy' or x == 'hard':
        break
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")


if x == "easy":
    attempts = 10

elif x == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: ")) 
    attempts -= 1
    if guess < number:
        print("Too Low.")
    elif guess > number:
        print("Too High.")
    else:
        print(f"You got it! The answer was {number}.")
        break


if guess != number:
    print(f"You've run out of guesses, you lose. The number was {number}.")