import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            result_label.config(text="Length must be a positive integer.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer for the length.")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter the desired length of the password:")
label_length.grid(row=0, column=0, padx=5, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=5, pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
