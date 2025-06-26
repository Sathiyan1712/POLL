# 🗳️ Polling Web App

This is a simple yet functional **polling website** built using **Django**, **SQLite**, **HTML/CSS**, and **Python**.

## 🚀 Features

- 👤 User registration & login system
- ✅ Create your own polls with multiple options
- 📊 Vote on polls created by others
- 🔒 Set a delete password while creating a poll to restrict deletion access
- 🧮 Live vote count displayed for each option
- 🧼 Clean, responsive UI using Bootstrap and custom CSS
- 📌 Only users who haven't voted can vote
- 📛 Only the person who knows the delete password can delete the poll

## 🏫 Use Cases

This app can be used in:

- ✅ Schools/Colleges – voting for Head Boy/Head Girl, Club Secretaries, etc.
- ✅ Office teams – voting on team decisions or nominations
- ✅ Any community-based decision making

## 🛠️ Built With

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS (Bootstrap)
- **Version Control:** Git + GitHub

## 📷 Screenshots

*Add screenshots here if you have any*

## 📦 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/Sathiyan1712/POLL.git
   cd POLL
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
