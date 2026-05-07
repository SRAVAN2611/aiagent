# 🤖 AI Agent (Smart Fallback System)

A simple Python AI chatbot using Google's Gemini API with automatic model fallback and retry handling.

This project intelligently switches between multiple Gemini models if one fails or becomes busy.

---

## 🚀 Features

- ✅ Gemini AI Integration
- ✅ Automatic Model Fallback
- ✅ Retry System for Busy Servers
- ✅ Colored Terminal UI
- ✅ Simple Interactive Chat
- ✅ Lightweight & Beginner Friendly

---

## 🧠 Models Used

The agent automatically tries models in this order:

1. `gemini-2.5-flash`
2. `gemini-2.0-flash`
3. `gemini-flash-latest`

If one model fails, it switches to the next available model automatically.

---

## 📂 Project Structure

```bash
aiagent/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SRAVAN2611/aiagent.git
cd aiagent
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

OR manually install:

```bash
pip install google-genai colorama
```

---

## 🔑 Setup API Key

Replace this line in the code:

```python
API_KEY = "YOUR_API_KEY"
```

with your Gemini API key.

Get API Key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run Project

```bash
python main.py
```

---

## 💻 Example Output

```bash
============================================================
        🤖 AI AGENT (SMART FALLBACK)
============================================================
Type 'exit' to quit

You ➤ Hello

Trying model: models/gemini-2.5-flash

Agent ➤ Hello! How can I help you today?
```

---

## 🔄 How Fallback Works

If a model:
- fails
- becomes overloaded
- returns server error (503)

The system:
1. retries the same model
2. switches to another Gemini model automatically

This makes the chatbot more reliable.

---

## 📦 requirements.txt

```txt
google-genai
colorama
```

---

## 🛡️ Important Security Note

❌ Never upload your real API key publicly.

Instead use:

```python
import os

API_KEY = os.getenv("GEMINI_API_KEY")
```

Then set environment variable:

### Windows

```bash
set GEMINI_API_KEY=your_api_key
```

### Linux/Mac

```bash
export GEMINI_API_KEY=your_api_key
```

---

## 🔧 Future Improvements

- Voice Assistant
- GUI Interface
- Memory Support
- Multi-Agent System
- Web Search Integration
- File Upload Support
- AI Tools Integration

---

## 👨‍💻 Author

Sravan V

GitHub:
https://github.com/SRAVAN2611

---

## ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
🐛 Report issues  
🚀 Contribute improvements

---

## 📜 License

This project is open-source and available under the MIT License.
