# 🎲 Number Guessing Game

A fun Python CLI game where the computer picks a random secret number between 1 and 10 and the player tries to guess it in as few attempts as possible.

## Features

- 🎯 Random number generation for each round
- 📉📈 "Too low" / "Too high" hints after each wrong guess
- 🔢 Attempt counter displayed upon winning
- 🔁 Option to play multiple rounds without restarting
- ✅ Robust input validation

## How to Run

```bash
python main.py
```

### Example Session

```
🎲 Welcome to the Number Guessing Game!
I have picked a number between 1 and 10. Can you guess it?

Enter a number between 1 and 10: 5
⬆️  Too high! Try a lower number.
Enter a number between 1 and 10: 3
⬇️  Too low! Try a higher number.
Enter a number between 1 and 10: 4

🎉 Congratulations! You guessed the correct number: 4
It took you 3 attempt(s).
```

## Requirements

- Python 3.6+
- No external dependencies

## Project Structure

```
number-guessing-game/
└── main.py   # Main script
```
