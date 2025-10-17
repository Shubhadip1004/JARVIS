# 🎙️ JARVIS Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

*A Python-powered voice assistant inspired by Tony Stark's JARVIS from Iron Man*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Available Commands](#%EF%B8%8F-available-commands) • [Project Structure](#%EF%B8%8F-project-structure) • [Technical Details](#-technical-details) • [Contributions](#-contributions) • [Troubleshooting](#-troubleshooting) • [License](#-license) • [Acknowledgment](#-acknowledgment)

</div>

---


<a id="features"></a>
## 🚀 Features

| Category | Features |
|----------|----------|
| **🎤 Voice Recognition** | Real-time speech-to-text using Vosk (offline) |
| **🔊 Speech Synthesis** | Text-to-speech responses with pyttsx3 |
| **📅 Date & Time** | Current date, time, and weekday information |
| **📰 News** | Latest technology news headlines |
| **😄 Entertainment** | Random dad jokes API with fallback jokes |
| **🖥️ System Control** | Launch applications (Windows) |
| **📁 File Management** | Open Documents and Downloads folders |
| **🌐 Web Integration** | Open websites and play YouTube music |
| **🤖 AI Chat** | GPT integration via OpenRouter for intelligent conversations |
| **🌐 Connection Monitoring** | Automatic internet detection with graceful offline fallback |
| **🔍 Smart Question Answering** | Ask questions and get AI-powered explanations |
| **📡 Online/Offline Mode** | Seamless switching between online and offline features |


<a id="installation"></a>
## 📦 Installation

  ### Prerequisites
   - Python 3.7 or higher
   - Windows OS (for app launching features)
   - Microphone
   - Internet connection (for news and jokes)

  ### Step-by-Step Setup

   1. **Clone the repository**

          git clone https://github.com/Shubhadip1004/JARVIS.git
   
          cd JARVIS

   2. **Install Python dependencies**

          pip install -r requirements.txt

   3. **Download Vosk Speech Recognition Model**

         *Download the model (choose one):*
         Small model (recommended):
   
            https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

            unzip vosk-model-small-en-us-0.15.zip

         *Or download manually from:*
      
            https://alphacephei.com/vosk/models

   4. **Set up environment variables**

         *Rename the example file:*
        
            cp .env.example .env

         *Add your API keys to .env:*

            Get free API keys from:

                 - OpenRouter: https://openrouter.ai/ for GPT access
      
                 - NewsAPI: https://newsapi.org/ for news headlines

            Your .env file should contain:

                   gpt_api_key=your_openrouter_api_key_here
      
                   news_api_key=your_newsapi_key_here



<a id="usage"></a>
## 🎯 Usage

   ### Starting JARVIS

         python src/main.py

   ### Example Interaction

         🎤 You: "Hello Jarvis"

         🔊 JARVIS: "Hello [Your Name]! How are you today?"

         🎤 You: "What time is it?"

         🔊 JARVIS: "Let me see... Current time is 14 hours, 25 minutes and 10 seconds"

         🎤 You: "Tell me a joke"

         🔊 JARVIS: "Why do programmers prefer dark mode? ... Because light attracts bugs!"


<a id="available-commands"></a>
## 🗣️ Available Commands

   ### Basic Commands

         "hello", "hi" - Greet JARVIS

         "what's your name" - Introduction

         "what time is it" - Current time

         "what's the date today" - Today's date

         "what day is it" - Current weekday

   ### Applications

         "open notepad" - Launch Notepad

         "open calculator" - Open Calculator

         "open browser" - Launch Chrome

         "open word" - Microsoft Word

         "open excel" - Microsoft Excel

         "open powerpoint" - Microsoft PowerPoint

         "open paint" - MS Paint

   ### Entertainment

         "tell me a joke" - Random dad joke

         "what's the news" - Technology headlines

         "play music" - YouTube music

   ### System & Web

         "open documents" - Documents folder

         "open downloads" - Downloads folder

         "open google" - Google search

         "open whatsapp" - WhatsApp Web

   ### Ask Questions

         "ask [question]" - AI-powered answers on any topic  
         
         "explain [concept]" - Detailed explanations  

<a id="project-structure"></a>
## 🏗️ Project Structure

      JARVIS/

            ├── src/

                  │   ├── main.py                 # 🎯 Main application entry point

                  │   ├── command.py              # ⚡ Command processing & execution

                  │   ├── live_transcriber.py     # 🎤 Voice recognition (Vosk)

                  │   ├── tts.py                  # 🔊 Text-to-speech engine

                  │   ├── jokes.py                # 😄 Joke API & fallback system

                  │   ├── news.py                 # 📰 News headlines fetcher

                  │   ├── date_and_time.py        # 📅 Date & time utilities

                  │   ├── connection_checker.py   # 🌐 Internet status & monitoring

                  │   ├── gpt_integration.py      # 🤖 AI chat with GPT models

                  │   └── state.py                # 🧠 Application state management

             ├── vosk-model-small-en-us-0.15/     # 🗣️ Speech model (download separately)

             ├── requirements.txt                 # 📦 Python dependencies

             ├── .env.example                     # 🔧 Environment template

             ├── .gitignore                       # 🙈 Git exclusion rules

             └── README.md                        # 📖 This file


## 🔧 Technical Details

   ### Voice Recognition

         Engine: Vosk (offline, no internet required)

         Model: vosk-model-small-en-us-0.15

         Sample Rate: 16kHz

         Latency: Real-time processing

   ### Text-to-Speech

         Library: pyttsx3 (cross-platform)

         Features: Offline operation, multiple voices

   ### External APIs

         News: NewsAPI (technology headlines)

         GPT: OpenAI (deepseek-r1t2-chimera model by tngtech)

         Jokes: icanhazdadjoke.com with fallback local jokes


## 🐛 Troubleshooting

   ### Common Issues

   **Microphone not detected:**

         Check microphone permissions

         Ensure default recording device is set

   **Vosk model not found:**

         Ensure model is in the correct location:
 
         JARVIS/vosk-model-small-en-us-0.15/

   **Dependencies installation failed:**

         Try installing individually:

               pip install vosk

               pip install sounddevice

               pip install pyttsx3

               pip install openai

   **News not working:**

         Verify NewsAPI key in .env file

         Check internet connection

   **GPT not working:**

         Verify GPT AI key in .env file

         Check internet connection

## 🤝 Contributions

   We welcome contributions! Feel free to:

      Fork the repository

      Create a feature branch (git checkout -b feature/AmazingFeature)

      Commit your changes (git commit -m 'Add some AmazingFeature')

      Push to the branch (git push origin feature/AmazingFeature)

      Open a Pull Request


## 📝 License

   This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments

      Vosk for offline speech recognition

      NewsAPI for news headlines

      OpenAI & tngtech for trained GPT model (deepseek-r1t2-chimera model)

      icanhazdadjoke for joke API

      Marvel's Iron Man for inspiration

<div align="center">
Made with ❤️ by Shubhadip Mahata

"Sometimes you gotta run before you can walk." - Tony Stark

</div>
