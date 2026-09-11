import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
recognizer = sr.Recognizer()

def speak(text):
    print("JARVIS:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "hello" in c:
        speak("Hello sir, how can I help you")

    else:
        speak("Sorry, I don't understand")


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print("Heard:", word)

            # Wake word
            if "jarvis" in word.lower():

                speak("Yes sir")

                # Command sunna
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)

                command = r.recognize_google(audio)
                print("You said:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timeout...")

        except sr.UnknownValueError:
            print("Could not understand...")

        except sr.RequestError:
            print("Google speech service error...")

        except Exception as e:
            print("Error:", e)