import pyttsx3
import random

def speak(text):
    engine = pyttsx3.init()  # create a fresh engine each time
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # optional, engine will be discarded anyway

def fallback_speech():
        fallback_speeches = ["I didn’t catch that. Please try again.",
    "Could you repeat that, please?",
    "Sorry, I missed that. Say it again.",
    "I’m not sure I understood you.",
    "Pardon me, could you speak again?",
    "I couldn’t hear that clearly.",
    "Hmm… that didn’t come through. Try again.",
    "I’m having trouble understanding you.",
    "Could you say that differently?",
    "I didn’t get that. Let’s try once more.",
    "I’m sorry, I didn’t understand your command.",
    "That didn’t make sense to me. Can you repeat?",
    "Oops, I didn’t hear that properly.",
    "Please say that again more clearly.",
    "I’m still listening… could you repeat that?"]
        return fallback_speeches[random.randint(0, len(fallback_speeches)-1)]
# speak("TTS module initialized.")
# speak("Hello, I am JARVIS, your personal AI assistant.")
# speak("How can I assist you today?")