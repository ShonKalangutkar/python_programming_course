import random

def play_guess_the_letter():
    min_ascii = ord('A') 
    max_ascii = ord('Z') 
    secret_ascii = random.randint(min_ascii, max_ascii)
    secret_letter = chr(secret_ascii)

    count = 0 

    print("Welcome to the Guess the Secret Letter Game!")
    print("I'm thinking of an uppercase letter between A and Z.")

    while True:
        try:
            player_guess = input("Type your letter (A-Z): ").strip().upper() 

            if len(player_guess) != 1 or not player_guess.isalpha():
                print("Invalid input! Please enter a single letter (A-Z).")
                continue 

            count += 1 

            if player_guess > secret_letter: 
                print("The letter comes *before* your guess in the alphabet.")
            elif player_guess < secret_letter:
                print("The letter comes *after* your guess in the alphabet.")
            else:
                print(f"Guessed right! The letter was {secret_letter}.")
                print(f"It took you {count} attempts.")
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    print("Thanks for playing!")

play_guess_the_letter()