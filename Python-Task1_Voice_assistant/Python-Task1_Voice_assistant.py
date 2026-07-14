import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import urllib.parse
import time
# -----------------------------
# Text To Speech
# -----------------------------
engine = pyttsx3.init(driverName="sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
recognizer = sr.Recognizer()
def speak(text):
    global engine

    print("Jarvis:", text)

    try:
        engine.stop()

        engine = pyttsx3.init(driverName="sapi5")

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)

        engine.say(text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print("Speech Error:", e)
# -----------------------------
# Listen
# -----------------------------
def listen():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.8)

            print("Speak now...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("Recognized:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Couldn't understand.")
        return ""

    except sr.RequestError:
        print("Internet connection error.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""
# -----------------------------
# Help Menu
# -----------------------------
def helpMenu():

    print("""
==================== JARVIS HELP ====================

You can say:

hello
hi
how are you
who are you
your name

time
date

search

open youtube
open gmail
open google
open chatgpt
open calculator
open notepad

tell me a joke

help

bye
exit
stop

=====================================================
""")

    speak("I have printed all commands on your screen.")

# -----------------------------
# Startup
# -----------------------------
print("Jarvis started.")
time.sleep(2)


speak("Hello! I am Jarvis.")
# -----------------------------
# Main Loop
# -----------------------------
while True:

    command = listen()

    if not command:
        continue

    # Greetings

    elif "hello" in command or "hi" in command:

        speak("Hello Vaishnavi.")
        time.sleep(1)
    elif "how are you" in command:

        speak("I am fine. What about you?")

    elif "who are you" in command:

        speak("I am Jarvis. Your Python Voice Assistant.")

    elif "your name" in command:

        speak("My name is Jarvis.")	
    elif "thank you" in command:

        speak("You're welcome Vaishnavi.")

    elif "good morning" in command:

        speak("Good Morning. Have a great day.")

    elif "good night" in command:

        speak("Good Night. Sweet dreams.")

    # -----------------------------
    # Time & Date
    # -----------------------------

    elif "time" in command:

        current = datetime.datetime.now().strftime("%I:%M %p")

        speak("Current time is " + current)

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak("Today's date is " + today)

    # -----------------------------
    # Google Search
    # -----------------------------

    elif "search" in command:

        speak("What do you want me to search?")

        query = listen()

        if query != "":

            speak("Searching Google for " + query)

            webbrowser.open(
                "https://www.google.com/search?q=" + 
                 urllib.parse.quote(query)
            )

    # -----------------------------
    # Open Websites
    # -----------------------------

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "open gmail" in command:

        speak("Opening Gmail")

        webbrowser.open("https://mail.google.com")

    elif "open chatgpt" in command:

        speak("Opening ChatGPT")

        webbrowser.open("https://chatgpt.com")

    # -----------------------------
    # Windows Apps
    # -----------------------------

    elif "open calculator" in command:

        speak("Opening Calculator")

        os.system("calc")

    elif "open notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")
    # -----------------------------
    # Jokes
    # -----------------------------

    elif "joke" in command:

        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "There are only 10 types of people. Those who understand binary and those who don't.",
            "Why did the computer go to the doctor? Because it had a virus.",
            "Debugging is like being a detective in a crime movie where you are also the criminal.",
            "I would tell you a UDP joke, but you might not get it."
        ]

        speak(random.choice(jokes))

    # -----------------------------
    # Help
    # -----------------------------

    elif "help" in command:

        helpMenu()

    # -----------------------------
    # Small Talk
    # -----------------------------

    elif "i am fine" in command:

        speak("That's great to hear.")

    elif "what can you do" in command:

        speak("I can tell the time and date, search Google, open YouTube, Gmail, Google, ChatGPT, Calculator, Notepad, tell jokes and chat with you.")

    elif "who made you" in command:

        speak("I was created by Vaishnavi using Python.")

    elif "goodbye" in command or "bye" in command:

        speak("See you later Vaishnavi.")
        break

    # -----------------------------
    # Exit
    # -----------------------------

    elif "exit" in command or "stop" in command:

        speak("Goodbye Vaishnavi. Have a nice day.")

        break

    # -----------------------------
    # Unknown Command
    # -----------------------------

    else:

        speak("Sorry. I don't know that command. Say help to see what I can do.")