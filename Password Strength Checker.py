import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def check_password_strength(password):

    # Define the password strength rules
    length_rule = len(password) >= 8
    upper_case_rule = any(char.isupper() for char in password)
    lower_case_rule = any(char.islower() for char in password)
    digit_rule = any(char.isdigit() for char in password)
    special_char_rule = bool(re.search(r"[!@#$%^&*()_+]", password))

    # Check the password against the rules
    if all([length_rule, upper_case_rule, lower_case_rule, digit_rule, special_char_rule]):
        return "Strong"

    elif all([upper_case_rule, lower_case_rule, digit_rule, special_char_rule]):
        return "Moderate"

    else:
        return "Weak"

def check_password():
    password = entry_password.get()

    if len(password) > 15:
        messagebox.showwarning("Password Length Warning", "Password more than 15 characters in length is not easy to remember, so it's not recommended.")
        return

    strength = check_password_strength(password)
    
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Set the initial size of the window to full screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Styling
style = ttk.Style()
style.theme_use('clam')  

style.configure('Button', padding=(10, 5, 10, 5), font=('Helvetica', 12), foreground='white', background='#4CAF50')
style.configure('TFrame', background='#6DB9EF')

# Create a frame for centering
frame = ttk.Frame(root, style='TFrame')
frame.pack(expand=True, fill='both', padx=20, pady=20)

title_label = ttk.Label(frame, text="Password Strength Checker", font=("Helvetica", 18, "bold"), foreground='#F4F27E', background='#3081D0')
title_label.grid(row=0, column=0, pady=20)

# Create GUI elements
label = ttk.Label(frame, text="Enter your password:", font=("Helvetica", 14), foreground='#F4F27E', background='#3081D0')
label.grid(row=1, column=0, pady=40)


entry_password = ttk.Entry(frame, show="", width=30, font=("Helvetica", 22))
entry_password.grid(row=2, column=0, pady=10)

check_button = ttk.Button(frame, text="Check Password", command=check_password)
check_button.grid(row=3, column=0, pady=10)


feedback_colors = {
    "Strong": "#4CAF50",  # Green
    "Moderate": "#FFC107",  # Yellow
    "Weak": "#FF5252",  # Red
}

feedback_label = ttk.Label(frame, text="", font=("Helvetica", 10))
feedback_label.grid(row=3, column=0, pady=5)
feedback_label.grid_remove()

# Educational Message
educational_message = tk.Label(frame, background='#6DB9EF', text="Tips for a strong password:\n- Use at least 8 characters.\n- Include a mix of upper and lower case letters.\n- Add digits and special characters for extra security.", font=("Helvetica", 15, "bold"), foreground='#333333')
educational_message.grid(row=4, column=0, pady=50, sticky="nsew")

# Ensure the grid layout expands properly
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Start the GUI application
root.mainloop()
