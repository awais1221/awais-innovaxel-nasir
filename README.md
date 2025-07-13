# awais-innovaxel-nasir
#  URL Shortener – Innovaxel Take-Home Assignment

This is a Django-based URL Shortener application that allows users to shorten long URLs, retrieve them, update or delete them, and view access statistics. A simple Bootstrap UI is included for ease of interaction.

---

## 🛠 Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/awais1221/awais-innovaxel-nasir.git
cd awais-innovaxel-nasir
git checkout dev

###  2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run Migrations

python manage.py makemigrations
python manage.py migrate


### 5. Start the Development Server

python manage.py runserver


### 6. Open in Browser

http://127.0.0.1:8000/


 Features
 Shorten long URLs

 Retrieve original URLs

 Update shortened URLs

 Delete shortened URLs

 View access count for each short URL

 Web-based frontend with Bootstrap

📂 Branch Structure
main: Contains only this README.md

dev: Contains the complete source code of the project

👤 Author
Muhammad Awais Nasir
Innovaxel Python Take-Home Assignment – 2025

vbnet
Copy
Edit

###  Next Step:

Run these commands to push it to your `main` branch:

```bash
git checkout main
git add README.md
git commit -m "Add setup instructions to main"
git push origin main



