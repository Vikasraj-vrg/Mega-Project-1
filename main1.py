import speech_recognition as sr
import webbrowser
import pyttsx3
import time


recognizer = sr.Recognizer()


def speak(text):
    print("JARVIS:", text)

    # Har baar naya voice engine
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()

    time.sleep(0.3)


def processCommand(command):

    command = command.lower().strip()

    print("YOU SAID:", command)

    if "open google" in command:
        speak("Open Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Open YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "hello" in command:
        speak("Hello sir, how can I help you")

    elif "who are you" in command:
        speak("I am Jarvis, your personal assistant")

    else:
        speak("Sorry sir, I did not understand your command")


# ==============================
# START JARVIS
# ==============================

speak("Initializing Jarvis")


while True:

    try:

        # -------------------------
        # LISTEN FOR JARVIS
        # -------------------------

        with sr.Microphone() as source:

            print("\nListening for Jarvis...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=3
            )

        word = recognizer.recognize_google(audio)

        print("HEARD:", word)

        # -------------------------
        # WAKE WORD
        # -------------------------

        if "jarvis" in word.lower():

            speak("Yes sir")

            time.sleep(0.5)

            # -------------------------
            # LISTEN FOR COMMAND
            # -------------------------

            with sr.Microphone() as source:

                print("Jarvis Active...")
                print("Speak your command...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            processCommand(command)


    except sr.WaitTimeoutError:

        print("Listening timeout...")


    except sr.UnknownValueError:

        print("I could not understand...")


    except sr.RequestError as e:

        print("Google error:", e)


    except Exception as e:

        print("ERROR:", e)

