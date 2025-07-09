# 📅 ETLab Assignment Reminder Bot

A Python automation tool that scrapes assignment deadlines from your college’s **ETLab** portal and syncs them to your **Google Calendar** — with automatic reminders so you never miss a deadline again.

---

## 🚀 Features

- ✅ Logs into ETLab using Selenium
- ✅ Scrapes assignments marked as **NOT SUBMITTED**
- ✅ Extracts subject name, start time, and due time
- ✅ Adds events to your **Google Calendar**
- ✅ Sets a **popup reminder 1 day before** the deadline

---

## 📦 Technologies Used

- 🐍 Python
- 🌐 Selenium
- 📅 Google Calendar API
- ⏰ datetime, pytz
- 🔐 OAuth 2.0 Authentication

---

## 📁 Project Structure
etlab-assignment-reminder/
├── etlab.py                 # Selenium scraper
├── google_calendar.py       # Calendar integration logic
├── credentials.json         # 🔒 Google API creds (not uploaded)
├── token.pkl                # 🔒 Saved login session
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
├── demo/                    # (Optional) Screenshots
└── .gitignore               # Hides sensitive files

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Abh0304/ECalSync.git
cd etlab-assignment-reminder
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```
### 3. Set Up Google Calendar API
	1.	Go to Google Cloud Console
	2.	Create a new project (e.g., ETLab Calendar)
	3.	Enable Google Calendar API
	4.	Create OAuth 2.0 Client ID (type: Desktop App)
	5.	Download the credentials.json file and place it in this project folder

### 4.Run the Script
```bash
python etlab.py
```
On the first run:
	•	A browser window opens asking you to sign in to Google
	•	Google Calendar access is authorized
	•	Events are added based on your pending assignments


 ## 🧠 Future Improvements
	•	Email or WhatsApp notifications using Twilio
	•	GUI using Tkinter or web frontend using Flask
	•	Cron-based daily sync
	•	Multi-semester support
	•	Assignment status updates in Google Calendar
