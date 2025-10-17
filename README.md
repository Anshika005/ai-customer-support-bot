# 💬 AI Support Bot by Anshika Mishra

An interactive **AI-powered customer support chatbot** built using **Flask**, **SQLite**, and **Google Gemini API**.  
The bot simulates a real support assistant that answers user queries, maintains chat history, and auto-detects when a conversation should be escalated to human support.

---

## 🚀 Features

- 🤖 AI-driven responses using **Google Gemini 2.0 Flash**
- 💾 Persistent chat sessions with **SQLite**
- ⚡ Real-time interaction using **Flask backend + JavaScript frontend**
- 🧠 Escalation logic for low-confidence answers
- 💬 Beautiful and responsive chat UI with typing animations
- 🧩 Quick-reply shortcut buttons for common queries
- 🕒 Context memory — remembers recent messages for better answers

---

## 🖼️ Screenshots
  

| Chat Interface | Typing Animation | Escalation Example |
| :-------------: | :--------------: | :----------------: |
| ![Chat UI](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20040350.png) | ![Typing](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20040427.png) | ![Escalation](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20035514.png) |
## 🖼️ Screenshots

### 💬 Chat Interface
![Chat UI](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20040350.png?raw=true)

---

### ⌨️ Typing Animation
![Typing](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20040427.png?raw=true)

---

### 🚨 Escalation Example
![Escalation](https://github.com/Anshika005/ai-customer-support-bot/blob/main/Screenshot%202025-10-17%20035514.png?raw=true)

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (via SQLAlchemy) |
| AI Model | Google Gemini 2.0 Flash |
| Environment | `.env` for secure API key storage |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally 👇

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/ai-support-bot.git
cd ai-support-bot
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` if not already present — suggested content below 👇)*

```
flask
flask_sqlalchemy
python-dotenv
google-generativeai
```

### 4️⃣ Add your Gemini API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 5️⃣ Run the Flask app

```bash
python app.py
```

Now open your browser and go to 👉
[`http://127.0.0.1:5000`](http://127.0.0.1:5000)

---

## 🧠 How It Works

1. A new session ID is created when the page loads.
2. User messages are saved to the database along with bot replies.
3. The bot builds conversation context and sends it to Gemini.
4. If the AI’s confidence is low (e.g., “I’m not sure”), the session is flagged for escalation.

---

## 🪄 Project Structure

```
├── app.py                 # Main Flask application
├── templates/
│   └── chatbot.html        # Frontend interface
├── chat_sessions.db        # SQLite database (auto-created)
├── .env                    # API key (not to be committed)
├── requirements.txt         # Dependencies list
└── README.md               # Project documentation
```

---

## 💡 Example Shortcuts

| Button              | Function                           |
| ------------------- | ---------------------------------- |
| **Business Hours**  | Shows store or service timings     |
| **Track Order**     | Simulates order tracking response  |
| **Pricing**         | Provides pricing or plan details   |
| **Contact Support** | Gives support contact information  |
| **Return Policy**   | Displays return/refund policy info |

---

## 🧑‍💻 Author

**👩‍💻 Anshika Mishra**
📍 CSE Student, VIT Bhopal
💌 [LinkedIn](#) · [GitHub](#)

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub — it really helps!

---

```

Frontend: HTML, CSS, JS
