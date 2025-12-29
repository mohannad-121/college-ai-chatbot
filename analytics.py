from flask import Blueprint, render_template
from models import ChatMessage

analytics = Blueprint("analytics", __name__)

@analytics.route("/dashboard")
def dashboard():
    total_chats = ChatMessage.query.count()
    return render_template("dashboard.html", total_chats=total_chats)
