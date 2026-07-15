import tkinter as tk
from tkinter import messagebox
import secrets
import string

# ---------------- Password History ----------------

history = []

# ---------------- Generate Password ----------------

def generate_password():

    length = int(length_spin.get())

    upper = upper_var.get()
    lower = lower_var.get()
    numbers = number_var.get()
    symbols = symbol_var.get()
    exclude = exclude_var.get()

    chars = ""
    password = []

    if upper:
        letters = string.ascii_uppercase
        if exclude:
            letters = letters.replace("O", "")
        chars += letters
        password.append(secrets.choice(letters))

    if lower:
        letters = string.ascii_lowercase
        if exclude:
            letters = letters.replace("l", "")
        chars += letters
        password.append(secrets.choice(letters))

    if numbers:
        nums = string.digits
        if exclude:
            nums = nums.replace("0", "").replace("1", "")
        chars += nums
        password.append(secrets.choice(nums))

    if symbols:
        sym = "!@#$%^&*()-_=+?"
        chars += sym
        password.append(secrets.choice(sym))

    if chars == "":
        messagebox.showwarning(
            "Error",
            "Select at least one character type."
        )
        return

    while len(password) < length:
        password.append(secrets.choice(chars))

    secrets.SystemRandom().shuffle(password)

    password = "".join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    history.insert(0, password)

    if len(history) > 5:
        history.pop()

    update_history()

    strength(password)

# ---------------- Password Strength ----------------

def strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*()-_=+?" for c in password):
        score += 1

    if score <= 2:
        strength_label.config(
            text="Weak",
            fg="red"
        )

    elif score <=4:
        strength_label.config(
            text="Medium",
            fg="orange"
        )

    else:
        strength_label.config(
            text="Strong",
            fg="green"
        )

# ---------------- Copy ----------------

def copy_password():

    pwd = password_entry.get()

    if pwd == "":
        return

    root.clipboard_clear()
    root.clipboard_append(pwd)

    messagebox.showinfo(
        "Copied",
        "Password copied successfully."
    )

# ---------------- History ----------------

def update_history():

    history_box.delete(0, tk.END)

    for item in history:
        history_box.insert(tk.END, item)

# ---------------- GUI ----------------

root = tk.Tk()

root.title("Advanced Password Generator")

root.geometry("450x550")

root.configure(bg="#f2f2f2")

title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Segoe UI",18,"bold"),
    bg="#f2f2f2"
)

title.pack(pady=15)

tk.Label(
    root,
    text="Password Length",
    bg="#f2f2f2"
).pack()

length_spin = tk.Spinbox(
    root,
    from_=8,
    to=50,
    width=10
)

length_spin.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Uppercase",
    variable=upper_var,
    bg="#f2f2f2"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Lowercase",
    variable=lower_var,
    bg="#f2f2f2"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var,
    bg="#f2f2f2"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbol_var,
    bg="#f2f2f2"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Exclude 0 O l 1",
    variable=exclude_var,
    bg="#f2f2f2"
).pack(anchor="w", padx=120)

tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    width=20
).pack(pady=15)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Consolas",12)
)

password_entry.pack()

tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    width=20
).pack(pady=10)

strength_label = tk.Label(
    root,
    text="Strength",
    font=("Segoe UI",12,"bold"),
    bg="#f2f2f2"
)

strength_label.pack()

tk.Label(
    root,
    text="Last 5 Passwords",
    bg="#f2f2f2"
).pack(pady=10)

history_box = tk.Listbox(
    root,
    width=40,
    height=5
)

history_box.pack()

root.mainloop()
