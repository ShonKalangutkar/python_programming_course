from random import randint

n = randint(1, 100)
count = 0          

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess_str = input("Type your number: ")
        guess = int(guess_str)

        if not (1 <= guess <= 100):
            print("Please enter a number between 1 and 100.")
            continue 

        count += 1

        if guess > n:
            print("The number is smaller.")
        elif guess < n:
            print("The number is bigger.")
        else:
            print(f"Guessed right! The number was {n}.")
            print(f"It took you {count} attempts.")
            break 

    except ValueError:
        print("Invalid input! Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")

print("Thanks for playing!")