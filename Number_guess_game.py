import random
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")

# Global variables
secret_number = 0
attempts = 0
attempt = 0
score = 100
difficulty = 1

# Function to start the game
def start_game():
    global secret_number, attempts, score, attempt, difficulty
    difficulty = difficulty_var.get()
    attempt = 0
    score = 100

    if difficulty == 1:
        secret_number = random.randint(1, 10)
        attempts = 6
    elif difficulty == 2:
        secret_number = random.randint(1, 50)
        attempts = 5
    elif difficulty == 3:
        secret_number = random.randint(1, 100)
        attempts = 4
    else:
        messagebox.showinfo("Invalid Choice", "Defaulting to Easy difficulty.")
        secret_number = random.randint(1, 10)
        attempts = 6

    # Move to the game layout
    open_game_layout()

# Function to handle guesses
def make_guess():
    global attempt, score
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if guess == 0:
        messagebox.showinfo("Game Over", "You quit the game!")
        root.quit()
        return

    if guess == secret_number:
        messagebox.showinfo("Congratulations!", f"You guessed the number! Final Score: {score}")
        root.quit()
        return

    score -= 10
    attempt += 1

    if attempt >= attempts:
        messagebox.showinfo("Game Over", f"Sorry, you've used all your attempts. The secret number was {secret_number}. Final Score: {score}")
        root.quit()
        return

    if guess < secret_number:
        feedback_label.config(text="📉 Too low! Try again.")
    else:
        feedback_label.config(text="📈 Too high! Try again.")

    # Update labels
    attempt_label.config(text=f"Attempt: {attempt + 1} of {attempts}")
    score_label.config(text=f"Score: {score}")
    guess_entry.delete(0, tk.END)

# Function to switch to the game layout
def open_game_layout():
    # Clear the current widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Game UI Elements
    game_info_label = tk.Label(root, text=f"You have {attempts} attempts to guess the number.\n"
                                          f"You start with a score of 100 points. Each wrong guess deducts 10 points.",
                               wraplength=300, justify="center")
    game_info_label.pack(pady=10)

    global attempt_label, score_label, guess_entry, feedback_label

    attempt_label = tk.Label(root, text=f"Attempt: {attempt + 1} of {attempts}")
    attempt_label.pack()

    score_label = tk.Label(root, text=f"Score: {score}")
    score_label.pack()

    guess_label = tk.Label(root, text="Enter your guess:")
    guess_label.pack()

    guess_entry = tk.Entry(root)
    guess_entry.pack()

    guess_button = tk.Button(root, text="Submit Guess", command=make_guess)
    guess_button.pack(pady=10)

    feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
    feedback_label.pack(pady=10)

# Main Menu UI Elements
title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

difficulty_label = tk.Label(root, text="Select Difficulty:")
difficulty_label.pack()

difficulty_var = tk.IntVar(value=1)
easy_radio = tk.Radiobutton(root, text="Easy (1-10)", variable=difficulty_var, value=1)
medium_radio = tk.Radiobutton(root, text="Medium (1-50)", variable=difficulty_var, value=2)
hard_radio = tk.Radiobutton(root, text="Hard (1-100)", variable=difficulty_var, value=3)
easy_radio.pack()
medium_radio.pack()
hard_radio.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Run the application
root.mainloop()