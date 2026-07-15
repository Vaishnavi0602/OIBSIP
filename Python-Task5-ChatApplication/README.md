# Simple Chat Application

A simple real-time chat application built using **Python**, **Socket Programming**, and **Tkinter**. The application allows multiple users to communicate over a local network through a graphical user interface.

## Oasis Infobyte Internship

**Domain:** Python Programming

**Task 5:** Chat Application

---

## Features

- User Login & Registration
- Real-time Messaging
- Multiple Clients Support
- Graphical User Interface (Tkinter)
- Local Network Communication
- Message History (JSON)
- User Authentication (JSON)
- Enter Key to Send Messages
- Emoji Support 😊😂❤️🔥
- Join & Leave Notifications
- Simple and Easy-to-Use Interface

---

## Technologies Used

- Python 3
- Socket Programming
- Tkinter
- Threading
- JSON
- OS Module

---

## Project Structure

```text
Python-Task5-ChatApplication/
│
├── server.py
├── client.py
├── users.json
├── messages.json
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Python-Task5-ChatApplication.git
```

Move into the project folder:

```bash
cd Python-Task5-ChatApplication
```

No external libraries are required.

---

## How to Run

### Step 1

Start the server:

```bash
python server.py
```

### Step 2

Open another terminal and run the client:

```bash
python client.py
```

### Step 3

Run multiple instances of `client.py` to chat between different users on the same computer or local network.

---

## How It Works

1. Register a new account or log in using an existing account.
2. Connect to the server.
3. Send and receive messages in real time.
4. Messages are automatically saved in `messages.json`.
5. Registered users are stored in `users.json`.
6. Notifications are shown when users join or leave the chat.

---

## Future Improvements

- Multiple Chat Rooms
- Private Messaging
- File Sharing
- Voice Messages
- Dark Mode
- Online User Status
- Emoji Picker
- Image Sharing

---

## Screenshots

Add screenshots of:

- Login Window
- Chat Window
- Multiple Clients Connected
- Join/Leave Notifications

---

## Author

**Vaishnavi Gangrade**

Computer Engineering Student  
Gujarat Technological University (GTU)  
Oasis Infobyte Python Programming Internship

---

## License

This project is developed for educational purposes as part of the **Oasis Infobyte Python Programming Internship**.