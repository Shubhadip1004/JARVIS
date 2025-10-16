import os
from dotenv import load_dotenv
import webbrowser
import time
from tts import speak, fallback_speech
from jokes import get_random_joke
from news import get_news_headlines
from date_and_time import date_today, current_time, weekday
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
        
    elif "date" in command or "today" in command:
        speak("Let me see...")
        time.sleep(0.4)
        speak("Today's date is " + date_today())
        state.unknown_command = 0
        
    elif "day" in command or "weekday" in command:
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
    
    elif "clock" in command or "time" in command or "alarm" in command:
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

    # Playing a YouTube video
    elif "you tube" in command:
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url)
        speak("Playing video on YouTube.")
        state.unknown_command = 0
        
    elif "music" in command or "song" in command:
        url = "https://www.youtube.com/watch?v=jvYNKUqMK_g&list=RDjvYNKUqMK_g&start_radio=1"
        webbrowser.open(url)
        speak("Playing music on YouTube.")
        state.unknown_command = 0
        
    elif "google" in command:
        url = "https://www.google.com"
        webbrowser.open(url)
        speak("Opening Google.")
        state.unknown_command = 0
        
    elif "whatsapp" in command or "whats app" in command or "message" in command:
        url = "https://web.whatsapp.com"
        webbrowser.open(url)
        speak("Opening WhatsApp.")
        state.unknown_command = 0

    # Telling jokes
    elif "joke" in command:
        [setup, punchline] = get_random_joke()
        speak(setup)    
        time.sleep(1.5)  # dramatic pause
        speak(punchline)
        state.unknown_command = 0
        
    elif "news" in command:
        load_dotenv()
        news_api_key = os.getenv("news_api_key")
        headlines = get_news_headlines(news_api_key)
        
        if headlines == ["Could not fetch news."] or headlines == ["No news articles found."]:
            speak(headlines[0])
            return
        
        speak("Here are the top news headlines on technology:")
        for idx, headline in enumerate(headlines, 1):
            speak(f"{idx}. {headline}")
            time.sleep(0.9)  # brief pause between headlines
        state.unknown_command = 0
    
    # Unknown command
    else:
        speak(fallback_speech())
        state.unknown_command += 1
        if state.unknown_command >= 3:
            time.sleep(1)
            speak("You can stop this conversation by pressing Control and C keys together.")
        