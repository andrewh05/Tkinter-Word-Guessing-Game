# Tkinter Word Guessing Game

## Overview

This project is a simple word-guessing game built with Python's Tkinter library. The game randomly selects a word from a list, scrambles its characters, and challenges the player to guess the original word. The player can request hints, which are revealed one character at a time. After entering their guess, the game checks if it’s correct or incorrect.

## Features
*Random Word Selection*: The game picks a word randomly from a predefined list.

*Scrambled Word Display*: The chosen word is displayed with its characters randomly shuffled. 

*Hints*: The player can request character-by-character hints for the chosen word.

*Answer Checking*: The player can enter their guess, and the game will verify if it's correct or incorrect.

*Pick Another Word*: The player can reset the game with a new randomly selected and shuffled word.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/tkinter-word-guessing-game.git
```

Navigate to the project directory:

```bash
cd tkinter-word-guessing-game
```

Install Python if you haven't already. You can download it from here.

(Optional) Create a virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

# Run the game:

```
python word_game.py
```

# Usage

Run the script and a window will open.
The window will display a scrambled word.
The player can:
Enter their guess in the text field.
Click "My Answer is" to check if their guess is correct.
Click "Hint" to get a character revealed from the original word.
Click "Pick Another" to reset the game with a new word.

# Example

Example: Scrambled word "niaforlcai" which is "california".

# Code Structure
Main File: `word_game.py` – Contains the entire logic for the game.

Functions:

**check_answer()**: Validates the user’s guess.

**hint()**: Reveals the next character in the original word.

**ran()**: Picks a new word, scrambles it, and resets the game.
