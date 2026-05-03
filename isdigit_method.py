import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    # Update labels
    user_label.config(text="You chose: " + user_choice)
    comp_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x300")

# Title label
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

# Buttons
btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

# Result labels
user_label = tk.Label(root, text="You chose: ")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer chose: ")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()