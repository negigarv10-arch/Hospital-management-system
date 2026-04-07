# 🏥 Moeka Hospital Management System
### Built with Python (Flask) + SQLite/MySQL + HTML/CSS

---

## 📁 Project Structure
```
hms/
├── app.py              ← Flask app entry point
├── config.py           ← Configuration (DB, secret key)
├── extensions.py       ← SQLAlchemy + LoginManager
├── models.py           ← Database models
├── seed.py             ← Creates admin + sample doctors
├── requirements.txt    ← Python dependencies
├── routes/
│   ├── auth.py         ← Login, Register, Logout
│   ├── patient.py      ← All patient features
│   ├── doctor.py       ← All doctor features
│   └── admin.py        ← All admin features
└── templates/
    ├── base.html        ← Shared layout
    ├── home.html        ← Landing page
    ├── select_login.html
    ├── patient/         ← Patient templates
    ├── doctor/          ← Doctor templates
    └── admin/           ← Admin templates
```

---

## ⚙️ Setup Instructions

### Step 1 — Install Python
Make sure Python 3.10 or above is installed.
Download from this: https://www.python.org/downloads/

### Step 2 — Create Virtual Environment (Recommended)
Open terminal/command prompt in the `hms` folder:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the App (uses SQLite by default)
```bash
python app.py
```
Open browser: http://127.0.0.1:5000

### Step 5 — Seed Sample Data (First time only)
Open a new terminal in the same folder:
```bash
python seed.py
```
This creates the default admin and 6 sample doctors.

---

## 🔑 Default Login Credentials

| Role    | ID        | Password  |
|---------|-----------|-----------|
| Admin   | ADMIN001  | admin123  |
| Doctor  | DOC001    | doc123    |
| Doctor  | DOC002    | doc123    |
| Patient | Register via /patient/register | - |

---

## 🗄️ Switch to MySQL (Optional)

1. Create a MySQL database:
```sql
CREATE DATABASE hms_db;
```

2. Set environment variable before running:
```bash
# Windows
set DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/hms_db

# Mac/Linux
export DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/hms_db
```

3. Then run:
```bash
python seed.py
python app.py
```

---

## 🧭 Features

### Patient
- Register with full details
- Login with Patient ID
- Book appointments with any doctor
- View appointment status (Pending / Confirmed / Cancelled)
- Cancel appointments
- Online payment with receipt
- View payment history
- View all doctors
- Update personal details

### Doctor
- Login with Doctor ID
- View profile and schedule
- View all appointments
- Confirm / Cancel appointments
- Add prescriptions for patients

### Admin
- Full dashboard with stats
- Add new doctors
- Update / Remove doctors
- View all patients
- Verify payment requests
- View monthly / yearly records

---

## 🛠️ Tech Stack

| Layer      | Technology            |
|------------|-----------------------|
| Backend    | Python 3.x + Flask    |
| Database   | SQLite (dev) / MySQL  |
| ORM        | SQLAlchemy            |
| Auth       | Flask-Login           |
| Frontend   | HTML + CSS (Jinja2)   |
| Icons      | Font Awesome 6        |
| Fonts      | Google Fonts (Nunito) |

---

## 📌 Notes

- Passwords are hashed using Werkzeug (never stored as plain text)
- SQLite database file `hms.db` is auto-created in the project folder
- All tables are auto-created on first run via `db.create_all()`
- The project follows the Incremental Process Model as per the SE document
