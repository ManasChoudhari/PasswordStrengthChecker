import tkinter as tk
from tkinter import messagebox
import string

class PasswordStrengthCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x400")

        # Labels and input field
        self.password_label = tk.Label(root, text="Enter Password:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)

        self.check_button = tk.Button(root, text="Check Password", command=self.check_password_strength)
        self.check_button.pack(pady=10)

        self.result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40, state=tk.DISABLED)
        self.result_text.pack(pady=10)

    def check_password_strength(self):
        password = self.password_entry.get()
        password_length = len(password)

        # Counters for different character types
        uppercase_count = sum(1 for c in password if c.isupper())
        lowercase_count = sum(1 for c in password if c.islower())
        digit_count = sum(1 for c in password if c.isdigit())
        special_count = sum(1 for c in password if c in string.punctuation)

        strength_percentage = 100.0
        char_set = set()

        if password_length < 8:
            self.display_result("Invalid Password: The password length must be at least 8 characters.")
            return

        # Adjust strength based on password length
        if password_length < 12:
            strength_percentage -= (12 - password_length) * 2.0
        elif password_length >= 20:
            strength_percentage += 5.0

        for char in password:
            if char in char_set:
                strength_percentage -= 2.0
            else:
                char_set.add(char)

        missing_characters = []
        if uppercase_count == 0:
            missing_characters.append("Uppercase character")
        if lowercase_count == 0:
            missing_characters.append("Lowercase character")
        if digit_count == 0:
            missing_characters.append("Digit")
        if special_count == 0:
            missing_characters.append("Special character")

        if missing_characters:
            self.display_result(f"The Strength of Password is Weak.\nMissing: {', '.join(missing_characters)}")
            return

        # Ensure the percentage does not go below 0
        strength_percentage = max(strength_percentage, 0.0)

        if strength_percentage >= 90.0:
            result = "The Strength of Password is Very Strong."
        elif strength_percentage >= 75.0:
            result = "The Strength of Password is Strong."
        elif strength_percentage >= 60.0:
            result = "The Strength of Password is Medium."
        elif strength_percentage >= 45.0:
            result = "The Strength of Password is Weak."
        else:
            result = "The Strength of Password is Very Weak."

        result += f"\n\nPassword Strength: {strength_percentage:.2f}%"
        self.display_result(result)

    def display_result(self, message):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthCheckerGUI(root)
    root.mainloop()
