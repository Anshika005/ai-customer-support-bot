import os
import uuid
import datetime
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise RuntimeError("Set GEMINI_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=GEMINI_KEY)
MODEL_NAME = "gemini-2.0-flash"

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat_sessions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ChatSession(db.Model):
    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    escalated = db.Column(db.Boolean, default=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.String, db.ForeignKey("chat_session.id"))
    role = db.Column(db.String)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

with app.app_context():
    db.create_all()

def build_context(session_id, limit=8):
    msgs = Message.query.filter_by(session_id=session_id).order_by(desc(Message.created_at)).limit(limit).all()
    msgs.reverse()
    context = ""
    for m in msgs:
        prefix = "User:" if m.role == "user" else "Bot:"
        context += f"{prefix} {m.text}\n"
    return context

def generate_reply(session_id, message):
    m = Message(session_id=session_id, role="user", text=message)
    db.session.add(m)
    db.session.commit()

    context = build_context(session_id)
    prompt = f"""You are a helpful customer support assistant.
If unsure, say you’re not sure and suggest escalation.
Conversation:
{context}
User: {message}
Assistant:"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    reply = response.text.strip()

    low_conf = any(kw in reply.lower() for kw in ["not sure", "cannot", "sorry", "don't know"])
    if len(reply) < 20:
        low_conf = True

    msg = Message(session_id=session_id, role="bot", text=reply)
    db.session.add(msg)

    if low_conf:
        sess = ChatSession.query.get(session_id)
        sess.escalated = True

    db.session.commit()
    return {"reply": reply, "escalated": low_conf}

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/session", methods=["POST"])
def session():
    sid = str(uuid.uuid4())
    s = ChatSession(id=sid)
    db.session.add(s)
    db.session.commit()
    return jsonify({"session_id": sid})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    sid = data.get("session_id")
    message = data.get("message")
    if not sid or not message:
        return jsonify({"error": "Missing data"}), 400
    return jsonify(generate_reply(sid, message))

if __name__ == "__main__":
    app.run(debug=True)
