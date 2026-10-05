# 🍅 Pomodoro Timer

A Python CLI implementation of the classic Pomodoro productivity technique. Set a focused work interval, and the timer counts down in real time, alerting you when it's time to take a break.

## Features

- ⏱️ User-defined work session duration (in minutes)
- 📺 Live countdown display that updates every second in-place
- 🔔 Clear notification when the session ends
- 🔁 Option to start additional sessions without restarting
- ✅ Input validation for non-integer and non-positive values

## How to Run

```bash
python main.py
```

### Example Session

```
🍅 Welcome to the Pomodoro Timer!
-----------------------------------
⏱️  Enter timer duration in minutes: 25

⏳ Timer started for 25 minute(s). Stay focused!

⌛ Time remaining: 24:59
...
🔔 Time's up! Take a short break. You earned it! ☕

Start another session? (yes/no): no

Goodbye! Keep up the great work. 💪
```

## Requirements

- Python 3.6+
- No external dependencies

## Project Structure

```
pomodoro-timer/
└── main.py   # Main script
```
