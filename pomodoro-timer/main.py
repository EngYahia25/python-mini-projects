"""
Pomodoro Timer
--------------
A simple CLI Pomodoro productivity timer. The user sets a work
interval in minutes and the timer counts down to zero.
"""

import time


def format_time(total_seconds: int) -> str:
    """Format a duration in seconds as MM:SS."""
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def run_timer(duration_minutes: int):
    """Count down from the given number of minutes to zero."""
    total_seconds = duration_minutes * 60

    print(f"\n⏳ Timer started for {duration_minutes} minute(s). Stay focused!\n")

    while total_seconds > 0:
        print(f"⌛ Time remaining: {format_time(total_seconds)}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    # Clear the countdown line before printing the final message
    print(" " * 40, end="\r")
    print("🔔 Time's up! Take a short break. You earned it! ☕")


def get_duration() -> int:
    """Prompt the user for a timer duration in minutes."""
    while True:
        try:
            minutes = int(input("⏱️  Enter timer duration in minutes: "))
            if minutes <= 0:
                print("Please enter a positive number of minutes.")
                continue
            return minutes
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """Main entry point for the Pomodoro Timer."""
    print("🍅 Welcome to the Pomodoro Timer!")
    print("-----------------------------------")

    while True:
        duration = get_duration()
        run_timer(duration)

        again = input("\nStart another session? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nGoodbye! Keep up the great work. 💪")
            break


if __name__ == "__main__":
    main()
