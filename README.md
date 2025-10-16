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
| ![Chat UI](<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/b948587d-c3f4-46ba-bb1e-9a3830686fdf" />
) | ![Typing](<img width="1916" height="970" alt="image" src="https://github.com/user-attachments/assets/07c39586-4848-43e4-8f4d-a82d0cf7e9f2" />
) | ![Escalation](<img width="1919" height="969" alt="image" src="https://github.com/user-attachments/assets/c3a877cd-b75c-4679-9a2c-87a12a80700e" />
) |

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

Deployment: Vercel (Serverless Functions)
