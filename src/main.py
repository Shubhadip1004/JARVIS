from tts import speak,fallback_speech
from live_transcriber import transcriber
from command import execute_command
import os
import sys  
import time
import random
from state import refresh_count

username = os.getlogin()

def main():
    speak(f"Hello {username}, I am your personal AI assistant, J.A.R.V.I.S.")
    speak("But you can call me Jarvis.")
    speak("I am an AI assistant. How can I help you today?")
    
    while True:
        try: 
            text = transcriber()
            if text:               # command recognized
                execute_command(text)
                refresh_count = 0  # reset on successful command
            else:                  # no command recognized
                speak(fallback_speech())
                refresh_count += 1
                if refresh_count >= 5:
                    if refresh_count == 5:
                        time.sleep(1)
                        speak("It seems we're having trouble understanding each other. Let's take a short break and try again later.")
                    time.sleep(2)  # pause for 2 seconds
                    if refresh_count == 10:
                        time.sleep(1)
                        speak("System shutting down")
                        sys.exit(0)
                
                elif refresh_count == 3:
                    time.sleep(1)
                    speak("If you need help, you can say things like 'open notepad', 'tell me a joke', or 'what's the news today?'")
                
                elif refresh_count == 4:
                    time.sleep(1)
                    wakeup_call = [
                    "Wake up, sir!",
                    "Wakey wakey, eggs and bakey!",
                    "Time to rise and shine!"
                    ]  
                    speak(random.choice(wakeup_call))
                
        except KeyboardInterrupt:
            speak(f"Goodbye {username}")
            print(f"Goodbye !!!  {username}")
            speak("Shutting down. Have a great day!")
            sys.exit(0)


if __name__ == "__main__":
    main()
        