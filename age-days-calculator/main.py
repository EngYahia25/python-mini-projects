"""
Age & Days Calculator
---------------------
Calculates the approximate number of days a person has lived
based on their age in years.
"""


DAYS_PER_YEAR = 365


def calculate_days(age: int) -> int:
    """Return the approximate number of days lived given age in years."""
    return age * DAYS_PER_YEAR


def get_age_input() -> int:
    """Prompt the user for their age and return it as an integer."""
    while True:
        try:
            age = int(input("Enter your age in years: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """Main entry point for the Age & Days Calculator."""
    print("--- Age in Days Calculator ---")
    age = get_age_input()
    days = calculate_days(age)
    print(f"You have lived for approximately {days:,} days.")


if __name__ == "__main__":
    main()
