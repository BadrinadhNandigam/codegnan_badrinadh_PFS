import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower()

    except Exception:
        print("Sorry, please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your virtual assistant. How can I help you?")

# Main Program
wish_user()

while True:
    command = take_command()

    if command == "":
        continue

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "wikipedia" in command:
        try:
            speak("Searching Wikipedia")
            query = command.replace("wikipedia", "").strip()

            if query == "":
                speak("Please tell me what to search.")
                continue

            result = wikipedia.summary(query, sentences=2)

            print("\nWikipedia Result:")
            print(result)

            speak("According to Wikipedia")
            speak(result)

        except Exception:
            speak("Sorry, I could not find information.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current Time:", current_time)
        speak(f"The time is {current_time}")

    elif "goodbye" in command or "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I don't understand that command.")