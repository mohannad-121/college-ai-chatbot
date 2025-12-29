 🤖 AI Chatbot Platform (Flask + NLP + ML)

A full-stack AI chatbot platform built using Flask, NLP, and Machine Learning, featuring authentication, admin dashboard, analytics, database persistence, and web deployment readiness.

This project demonstrates an end-to-end chatbot system: from model logic to frontend UI and deployment.

------------------------

Features

- 🤖 Intelligent chatbot (NLP-based intent classification)
- 👥 Multi-user chat history (database persistence)
- 🔐 Authentication system (login / logout)
- 🧑‍💼 Admin panel (role-based access)
- 📊 Analytics dashboard
- 🎤 Voice input (browser-based)
- 🕒 Message timestamps
- 🎨 Professional web interface
- 🗄 Database using SQLAlchemy
- ☁️ Deployment-ready (Render / Railway)

------------------

 Project Structure

project-root/
│
├── app.py
├── config.py
├── models.py
├── auth.py
├── admin.py
├── chatbot_logic.py
├── analytics.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── chat.html
│   ├── admin.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   │   ├── chat.js
│   │   └── dashboard.js
│   └── images/
│       ├── chatbot1.png
│       └── chatbot2.png
│
└── database.db

-----------------

Technologies Used

Backend: Flask, Flask-Login, Flask-SQLAlchemy
AI / NLP: NLTK, Scikit-learn
Machine Learning: TensorFlow / PyTorch (optional)
Frontend: HTML, CSS, JavaScript
Database: SQLite (upgradeable to PostgreSQL)
Deployment: Render / Railway

---

⚙️Installation & Setup

Clone Repository

git clone https://github.com/your-username/your-repo-name.git  
cd your-repo-name

-------------------

 2. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

 3. Install Dependencies

pip install -r requirements.txt

---

 4. Download NLTK Data (first run only)

python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')

---

# 5. Run Application

python app.py

Open browser:
http://127.0.0.1:5000

---------------------

 🔐 Login System

- Users authenticate using username & password
- Passwords are securely hashed
- Admin users have access to:
  - Admin dashboard
  - Analytics panel
  - User management

---------------------

 📊 Analytics
The dashboard displays:
- Total messages
- Active users
- Message history
- Usage statistics

---

 🧠 Improving Chatbot Accuracy

To improve responses:

1. Add more intent data
2. Improve preprocessing in chatbot_logic.py
3. Replace classic ML with Transformer-based models
4. Fine-tune models instead of rule-based replies

After updates, simply restart:

python app.py

---

 ☁️ Deployment (Render)

1. Push project to GitHub
2. Go to https://render.com
3. Create New Web Service
4. Connect GitHub repository
5. Build command:
   pip install -r requirements.txt
6. Start command:
   python app.py
7. Set Python version to 3.10

---

 🌐 Custom Domain (Paid)

1. Buy domain (Namecheap / GoDaddy)
2. Go to Render → Settings → Custom Domains
3. Add domain
4. Update DNS records
5. SSL enabled automatically

---

📌 Future Enhancements

- Mobile app version
- Cloud GPU inference
- Advanced LLM integration
- Paid user plans
- Chat export & monitoring

---

 👨‍💻 Author

Developed by: Mohannad Abuayyash  
AI & Software Engineering Project

----------

📝 License

This project is for educational and demonstration purposes.
