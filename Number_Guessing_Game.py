import random

attempts = 10
best_score = None
print("Welcome to the Number Guessing Game!")
min_score = int(input("Enter the minimum number of range: "))
max_score = int(input("Enter the maximum number of range: "))
number_to_guess = random.randint(min_score, max_score)
while True:
    try:
        if attempts == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}.")
            break
        guess = int(input(f"Enter a number between {min_score} and {max_score}: "))
        if guess == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif guess > number_to_guess:
            print("Too high!")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        elif guess < number_to_guess:
            print("Too low!")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if best_score is None or attempts > best_score:
    best_score = attempts
    print(f"New best score: {best_score} attempts remaining!")

    
