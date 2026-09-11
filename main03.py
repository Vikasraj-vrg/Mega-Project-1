
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime


# ==============================
# VRG VOICE ASSISTANT
# ==============================

ASSISTANT_NAME = "Gautam"


# ==============================
# TEXT TO SPEECH
# ==============================

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Gautam:", text)

    engine.say(text)
    engine.runAndWait()


# ==============================
# SPEECH RECOGNITION
# ==============================

recognizer = sr.Recognizer()

recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300


def listen():

    with sr.Microphone() as source:

        print("\n🎙️ Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:

            print("No voice detected.")
            return ""

    try:

        print("🔄 Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:

        print("❌ Could not understand.")
        return ""

    except sr.RequestError:

        print("❌ Internet/Speech service problem.")
        return ""

    except Exception as e:

        print("Error:", e)
        return ""


# ==============================
# COMMAND PROCESSING
# ==============================

def process_command(command):

    # GOOGLE
    if "google" in command:

        speak("Opening Google.")

        webbrowser.open(
            "https://www.google.com"
        )


    # YOUTUBE
    elif "youtube" in command:

        speak("Opening YouTube.")

        webbrowser.open(
            "https://www.youtube.com"
        )


    # CHATGPT
    elif "chatgpt" in command:

        speak("Opening ChatGPT.")

        webbrowser.open(
            "https://chatgpt.com"
        )


    # TIME
    elif "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}"
        )


    # DATE
    elif "date" in command:

        today = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        speak(
            f"Today's date is {today}"
        )


    # HELLO
    elif "hello" in command or "hi" in command:

        speak(
            "Hello sir. How can I help you?"
        )


    # HOW ARE YOU
    elif "how are you" in command:

        speak(
            "I am fine sir."
        )


    # WHO ARE YOU
    elif "who are you" in command:

        speak(
            "I am VRG, your personal voice assistant."
        )


    # EXIT
    elif (
        "exit" in command
        or "quit" in command
        or "stop" in command
        or "close" in command
    ):

        speak(
            "Okay sir. Goodbye."
        )

        return False


    # UNKNOWN
    else:

        speak(
            "Sorry sir, I don't know that command yet."
        )


    return True


# ==============================
# MAIN PROGRAM
# ==============================

def main():

    speak(
        "Hello sir. I am Gautam."
    )

    speak(
        "I am ready for your command."
    )


    while True:

        command = listen()

        if command == "":
            continue

        running = process_command(command)

        if not running:
            break


# ==============================
# START
# ==============================

if __name__ == "__main__":

    main()

