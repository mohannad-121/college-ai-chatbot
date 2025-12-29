from flask import Flask, request, jsonify, render_template
from flask_login import LoginManager, login_required, current_user
from config import Config
from models import db, User, ChatMessage
from auth import auth
from admin import admin
from analytics import analytics
from chatbot_logic import chatbot_reply
import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(analytics)

@app.route("/chat")
@login_required
def chat():
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
@login_required
def api_chat():
    msg = request.json["message"]
    reply = chatbot_reply(msg)

    chat = ChatMessage(
        user_id=current_user.id,
        message=msg,
        response=reply
    )
    db.session.add(chat)
    db.session.commit()

    return jsonify({"reply": reply})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
