import random

# Game set up
print("Welcome to the guessing game!")
number_of_guesses = 3  # User hat 3 guesses before losing the game
user_won = False

# Computer guesses a random number between 1 and 10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
    # User guesses the number
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)

    # Computer tells user whether guess was too high or too low
    if user_guess == correct_answer:
        print("Good guess!")
        print("You are correct!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Sorry, you guessed too high!")
    elif user_guess < correct_answer:
        print("Sorry, you guessed too low!")

    number_of_guesses -= 1

if user_won == True:
    print("You won!")
else:
    print("You lost!")
