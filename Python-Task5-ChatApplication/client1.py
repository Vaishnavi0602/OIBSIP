import tkinter as tk
from tkinter import messagebox
import socket
import threading
import json
import os

HOST = "127.0.0.1"
PORT = 5555

USERS_FILE = "users.json"
HISTORY_FILE = "messages.json"

# ---------------- JSON ----------------

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

with open(USERS_FILE, "r") as f:
    users = json.load(f)

with open(HISTORY_FILE, "r") as f:
    history = json.load(f)

# ---------------- LOGIN ----------------

username = ""

login = tk.Tk()
login.title("Simple Chat Login")
login.geometry("300x220")

tk.Label(login, text="Username").pack(pady=5)
username_entry = tk.Entry(login)
username_entry.pack()

tk.Label(login, text="Password").pack(pady=5)
password_entry = tk.Entry(login, show="*")
password_entry.pack()

mode = tk.StringVar(value="Login")

tk.Radiobutton(login, text="Login", variable=mode, value="Login").pack()
tk.Radiobutton(login, text="Register", variable=mode, value="Register").pack()

# ---------------- LOGIN FUNCTION ----------------

def continue_login():

    global username

    u = username_entry.get().strip()
    p = password_entry.get().strip()

    if u == "" or p == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    if mode.get() == "Register":

        if u in users:
            messagebox.showerror("Error", "User already exists")
            return

        users[u] = p

        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

    else:

        if u not in users or users[u] != p:
            messagebox.showerror("Error", "Invalid Login")
            return

    username = u

    login.destroy()

tk.Button(
    login,
    text="Continue",
    command=continue_login,
    width=18
).pack(pady=10)

login.mainloop()

# ---------------- CHAT ----------------

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

window = tk.Tk()
window.title("Simple Chat")
window.geometry("600x450")

chat = tk.Text(window, state="normal")
chat.pack(fill="both", expand=True)

# Load history

for msg in history:
    chat.insert(tk.END, msg + "\n")

entry = tk.Entry(window)
entry.pack(fill="x")

# ---------------- RECEIVE ----------------

def receive():

    while True:

        try:

            message = client.recv(1024).decode()

            chat.insert(tk.END, message + "\n")
            chat.see(tk.END)

            history.append(message)

            with open(HISTORY_FILE, "w") as f:
                json.dump(history, f, indent=4)

        except:
            break

# ---------------- SEND ----------------

def send(event=None):

    msg = entry.get().strip()

    if msg == "":
        return

    message = f"{username}: {msg}"

    client.send(message.encode())

    chat.insert(tk.END, message + "\n")
    chat.see(tk.END)

    history.append(message)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

    entry.delete(0, tk.END)

tk.Button(
    window,
    text="Send",
    command=send
).pack()

entry.bind("<Return>", send)

threading.Thread(
    target=receive,
    daemon=True
).start()

window.mainloop()