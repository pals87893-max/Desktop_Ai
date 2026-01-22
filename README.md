# 🎙️ Lisaara – Python Voice Assistant

Lisaara is a Python-based voice assistant that can listen to voice commands, respond using AI, open applications, perform web searches, and speak responses using text-to-speech.

---

## ✨ Features

- 🎤 Voice input using Speech Recognition
- 🗣️ Text-to-Speech output (Windows SAPI)
- 🤖 AI-powered responses using Groq LLM
- 🕒 Tells current time
- 🖥️ Opens desktop applications
- 🌐 Opens popular websites via voice commands
- 📁 Saves AI command responses to files
- 🔊 Wake-word based commands (`hey`)

---

## 🛠️ Technologies Used

- Python 3.x
- `speech_recognition`
- `pywin32`
- `AppOpener`
- `groq`
- Windows SAPI (Text-to-Speech)
- Google Speech Recognition API

---

## 📦 Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/pals87893-max/Desktop_Ai.git
cd lisaara-voice-assistant
pip install requirements.txt
```

🔑 Environment Setup
Set Groq API Key (Required)

▶️ Usage

Run the assistant:
python main.py

You will hear:

Hello, I am Lisaara

🗣️ Voice Commands
open chrome	Opens an application
what is the time	Speaks current time
search youtube	Opens YouTube
hey explain python	AI-generated response saved to file
stop	Exits the assistant


⚠️ Known Limitations

Works on Windows only
Requires an active internet connection
Speech recognition accuracy depends on microphone quality

🚀 Future Improvements

Wake-word detection
Background execution
Offline speech recognition
Long-term memory support
GUI interface


📄 License

This project is licensed under the MIT License.

👤 Author

sumit Pal

⭐ If you like this project, don’t forget to star the repo!
