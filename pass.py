import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a positive number.")
        else:
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid number.")


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Password:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.grid(row=1, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2, padx=10, pady=5)


length_entry.focus()


root.mainloop()


