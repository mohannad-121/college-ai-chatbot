from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import User, ChatMessage

admin = Blueprint("admin", __name__)

@admin.route("/admin")
@login_required
def admin_panel():
    if current_user.role != "admin":
        return "Access denied", 403
    users = User.query.all()
    chats = ChatMessage.query.all()
    return render_template("admin.html", users=users, chats=chats)
