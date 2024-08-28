import tkinter as tk
import re

def check_strength(pwd):
    """Check password strength based on criteria."""
    if len(pwd) < 8:
        return "Weak: At least 8 characters."
    if not re.search(r"[a-z]", pwd):
        return "Weak: Include a lowercase letter."
    if not re.search(r"[A-Z]", pwd):
        return "Weak: Include an uppercase letter."
    if not re.search(r"\d", pwd):
        return "Weak: Include a number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        return "Weak: Include a special character."
    return "Strong: Meets all criteria."

def assess():
    """Evaluate password and display result."""
    pwd = entry.get()
    result.set(check_strength(pwd))

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker")

# GUI elements
tk.Label(root, text="Password:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root, show='*', width=40)
entry.grid(row=0, column=1, padx=10, pady=5)

result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Check Strength", command=assess).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

