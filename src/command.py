import os
from dotenv import load_dotenv
import webbrowser
import time
from tts import speak, fallback_speech
from jokes import get_random_joke
from news import get_news_headlines
from date_and_time import date_today, current_time, weekday
from gpt_integration import ask_model
from connection_checker import is_online, connection_message
import state



username = os.getlogin()

def execute_command(command):
    command = command.lower()

    # Greetings
    
    if "hello" in command or "hi" in command:
        speak(f"Hello {username}! How are you today?")
        state.unknown_command = 0
    
    elif "can you do" in command or "you do" in command:
        speak("I can tell you the current date and time, open applications and folders, play YouTube videos, tell jokes, and give you the latest news headlines.")
        state.unknown_command = 0
    
    elif "name" in command:
        speak(f"Hello, {username}")
        time.sleep(0.4)
        speak("I am JARVIS, your personal AI assistant.")
        state.unknown_command = 0
    
    # Date and Time
    
    elif "date" in command or "today" in command:
        speak("Let me see...")
        time.sleep(0.4)
        speak("Today's date is " + date_today())
        state.unknown_command = 0
        
    elif "day" in command or "weekday" in command or "week day" in command:
        speak("Let me see...")
        time.sleep(0.4)
        speech = "Today is " + weekday()
        speak(speech)
        state.unknown_command = 0
    
    elif "time" in command:
        speak("Let me see...")
        time.sleep(0.4)
        speech = "Current time is " + current_time()
        speak(speech)
        state.unknown_command = 0
        
    # Opening apps (Windows example)
    
    elif "notepad" in command:
        os.system("start notepad")
        speak("Opening Notepad.")
        state.unknown_command = 0
    
    elif "paint" in command:
        os.system("start mspaint")
        speak("Opening Paint.")
        state.unknown_command = 0
        
    elif "word" in command:
        os.system("start winword")
        speak("Opening Microsoft Word.")
        state.unknown_command = 0
    
    elif "excel" in command:   
        os.system("start excel")
        speak("Opening Microsoft Excel.")
        state.unknown_command = 0
    
    elif "power point" in command or "powerpoint" in command:       
        os.system("start powerpnt")
        speak("Opening Microsoft PowerPoint.")
        state.unknown_command = 0
    
    elif "browser" in command or "chrome" in command:
        os.system("start chrome")
        speak("Opening Google Chrome.")
        state.unknown_command = 0
    
    elif "clock" in command or "alarm" in command:
        os.system("start ms-clock:")
        speak("Opening Alarms and Clock.")
        state.unknown_command = 0
        
    elif "calculator" in command:
        os.system("start calc")
        speak("Opening Calculator.")
        state.unknown_command = 0
    
    # Opening folders
    elif "documents" in command or "document" in command:
        folder_path = f"C:\\Users\\{username}\\Documents"
        os.startfile(folder_path)
        speak(f"Opening your Documents folder.")
        state.unknown_command = 0
    
    elif "downloads" in command or "download" in command:
        folder_path = f"C:\\Users\\{username}\\Downloads"
        os.startfile(folder_path)
        speak(f"Opening your Downloads folder.")
        state.unknown_command = 0

    # Opening websites
    
    elif "you tube" in command:
        state.unknown_command = 0
        if is_online():
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            webbrowser.open(url)
            speak("Playing video on YouTube.")
        else:
            speak("I need an internet connection to play videos.")
            state.offline_count += 1
            
        speak(connection_message(state.offline_count))

    elif "music" in command or "song" in command:
        state.unknown_command = 0
        if is_online():
            url = "https://www.youtube.com/watch?v=jvYNKUqMK_g&list=RDjvYNKUqMK_g&start_radio=1"
            webbrowser.open(url)
            speak("Playing music on YouTube.")
        else:
            speak("I need an internet connection to play music.")
            state.offline_count += 1
        
        speak(connection_message(state.offline_count))

    elif "google" in command:
        state.unknown_command = 0
        if is_online():
            url = "https://www.google.com"
            webbrowser.open(url)
            speak("Opening Google.")
            state.offline_count = 0
        else:
            speak("I need an internet connection to open Google.")
            state.offline_count += 1
        
        speak(connection_message(state.offline_count))

    elif "whatsapp" in command or "whats app" in command or "message" in command:
        state.unknown_command = 0
        if is_online():
            url = "https://web.whatsapp.com"
            webbrowser.open(url)
            speak("Opening WhatsApp.")
            state.offline_count = 0
        else:
            speak("I need an internet connection to open WhatsApp.")
            state.offline_count += 1
            
        speak(connection_message(state.offline_count))

    # Telling jokes
    
    elif "joke" in command:
        if not is_online():
            state.offline_count += 1
            
        else:
            state.offline_count = 0
        
        [setup, punchline] = get_random_joke(is_online())
        speak(setup)    
        time.sleep(1.5)  # dramatic pause
        speak(punchline)
        state.unknown_command = 0
        
        if state.offline_count >= 6:
            speak("You can hear more jokes by connecting to the internet.")
        
    # Implementing GPT functionality

    elif "ask" in command or "question" in command or "explain" in command or "explanation" in command:
        state.unknown_command = 0
        if is_online():    
            load_dotenv()
            gpt_api_key = os.getenv("gpt_api_key")
            speak("What would you like to ask?")
            time.sleep(0.5)
            user_question = input("Your question: ")
            speak("Let me think about that...")
            response = ask_model(user_question,gpt_api_key)
            speak(response)
            state.offline_count = 0
        else:
            speak("I need an internet connection to answer that.")
            state.offline_count += 1
            
        speak(connection_message(state.offline_count))
    
    # Getting news headlines
    
    elif "news" in command:
        load_dotenv()
        news_api_key = os.getenv("news_api_key")
        headlines = get_news_headlines(news_api_key, is_online=is_online())
        
        state.unknown_command = 0
        if not is_online() or headlines == ["No news articles found."]:
            speak(headlines[0])
            state.offline_count += 1
        else:
            speak("Here are the top news headlines on technology:")
            time.sleep(0.4)
            for headline in headlines:
                speak(f"{headline}")
                time.sleep(0.9)  # brief pause between headlines
            state.offline_count = 0
        
        speak(connection_message(state.offline_count))
    
    # exit command
    
    elif "exit" in command or "quit" in command or "bye" in command or "goodbye" in command:
        speak(f"Goodbye {username}!")
        time.sleep(0.4)
        speak("Shutting down. Have a great day!")
        os._exit(0)
    
    
    # Unknown command
    
    else:
        speak(fallback_speech())
        state.unknown_command += 1
        if state.unknown_command >= 3:
            time.sleep(1)
            speak("You can stop this conversation by saying quit or exit.")
        
