# 🌐 Socialize

**Socialize** is a platform that allows you to manage and schedule posts across multiple social media accounts — all from one unified dashboard. Currently supports **Reddit** and **Telegram**.

## 🚀 Features

- 🔐 User authentication
- 📝 Schedule Reddit posts with title, body & media
- 📤 Schedule Telegram messages with media support
- ⏳ Preview posts before publishing
- 🗂 View and manage scheduled content
- ⚙️ Background job queue using Celery + Redis
- 📅 Periodic task management with Celery Beat
- 💻 Clean Bootstrap-based UI

---

## 🛠 Tech Stack

- **Backend:** Django
- **Asynchronous Task Queue:** Celery + Redis
- **Scheduler:** Celery Beat
- **Frontend:** Bootstrap
- **Containerization:** Docker (Optional)

---

## ⚙️ Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/SAMurai-16/Socialize.git
cd Socialize
```
### 2. Create a virtual environment and activate it
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a .env file in the root directory with the necessary keys for your Reddit and Telegram APIs. 

### 5. Run database migrations
```bash
python manage.py migrate
```
### 6.  Run Redis (make sure it’s installed and running)

### 7. Start Celery Workers
```bash
celery -A social_scheduler worker --loglevel=info
celery -A social_scheduler beat --loglevel=info
```
### 8. Start the Django Server
```bash
python manage.py runserver
```
