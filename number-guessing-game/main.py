"""
Number Guessing Game
--------------------
A simple CLI game where the player tries to guess a randomly
generated secret number between 1 and 10.
"""

import random


MIN_NUMBER = 1
MAX_NUMBER = 10


def get_guess(min_val: int, max_val: int) -> int:
    """Prompt the player for a valid integer guess within the given range."""
    while True:
        try:
            guess = int(input(f"Enter a number between {min_val} and {max_val}: "))
            if min_val <= guess <= max_val:
                return guess
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Run a single round of the Number Guessing Game."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print("🎲 Welcome to the Number Guessing Game!")
    print(f"I have picked a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?\n")

    while True:
        guess = get_guess(MIN_NUMBER, MAX_NUMBER)
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Congratulations! You guessed the correct number: {secret}")
            print(f"It took you {attempts} attempt(s).")
            break
        elif guess < secret:
            print("⬆️  Too low! Try a higher number.")
        else:
            print("⬇️  Too high! Try a lower number.")


def main():
    """Main entry point for the Number Guessing Game."""
    play_game()

    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again in ("yes", "y"):
            play_game()
        elif play_again in ("no", "n"):
            print("Thanks for playing! Goodbye. 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
