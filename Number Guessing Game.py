import random

# Generate a random number
secret_number = random.randint(1, 100)
max_attempts = 5
attempts = 0

# Game loop
while attempts < max_attempts:
    guess = int(input("Enter your guess (between 1 and 100): "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
    
    attempts += 1

if attempts == max_attempts:
    print(f"Game over! The secret number was {secret_number}.")
