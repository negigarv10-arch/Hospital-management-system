from extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# ─── PATIENT ──────────────────────────────────────────────────────────────────
class Patient(UserMixin, db.Model):
    __tablename__ = 'patient'
    id          = db.Column(db.Integer, primary_key=True)
    p_id        = db.Column(db.String(20), unique=True, nullable=False)
    name        = db.Column(db.String(100), nullable=False)
    dob         = db.Column(db.String(20))
    gender      = db.Column(db.String(10))
    blood_group = db.Column(db.String(5))
    email       = db.Column(db.String(100), unique=True)
    mobile      = db.Column(db.String(15))
    address     = db.Column(db.String(200))
    category    = db.Column(db.String(20), default='Private')  # CGHS or Private
    card_pic    = db.Column(db.String(200))
    password    = db.Column(db.String(200), nullable=False)
    role        = db.Column(db.String(10), default='patient')

    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    bills        = db.relationship('Bill', backref='patient', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return f"patient_{self.id}"


# ─── DOCTOR ───────────────────────────────────────────────────────────────────
class Doctor(UserMixin, db.Model):
    __tablename__ = 'doctor'
    id             = db.Column(db.Integer, primary_key=True)
    d_id           = db.Column(db.String(20), unique=True, nullable=False)
    name           = db.Column(db.String(100), nullable=False)
    age            = db.Column(db.Integer)
    gender         = db.Column(db.String(10))
    specialization = db.Column(db.String(100))
    experience     = db.Column(db.String(50))
    language       = db.Column(db.String(100))
    mobile         = db.Column(db.String(15))
    email          = db.Column(db.String(100), unique=True)
    schedule       = db.Column(db.String(200))
    consultant_fee = db.Column(db.Float, default=0.0)
    password       = db.Column(db.String(200), nullable=False)
    role           = db.Column(db.String(10), default='doctor')
    photo          = db.Column(db.String(200))

    appointments  = db.relationship('Appointment', backref='doctor', lazy=True)
    prescriptions = db.relationship('Prescription', backref='doctor', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return f"doctor_{self.id}"


# ─── ADMIN ────────────────────────────────────────────────────────────────────
class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id       = db.Column(db.Integer, primary_key=True)
    a_id     = db.Column(db.String(20), unique=True, nullable=False)
    name     = db.Column(db.String(100), nullable=False)
    dob      = db.Column(db.String(20))
    gender   = db.Column(db.String(10))
    email    = db.Column(db.String(100), unique=True)
    mobile   = db.Column(db.String(15))
    address  = db.Column(db.String(200))
    password = db.Column(db.String(200), nullable=False)
    role     = db.Column(db.String(10), default='admin')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return f"admin_{self.id}"


# ─── APPOINTMENT ──────────────────────────────────────────────────────────────
class Appointment(db.Model):
    __tablename__ = 'appointment'
    id             = db.Column(db.Integer, primary_key=True)
    patient_id     = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id      = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    specialization = db.Column(db.String(100))
    date           = db.Column(db.String(20))
    time           = db.Column(db.String(20))
    consultant_fee = db.Column(db.Float)
    status         = db.Column(db.String(20), default='Pending')   # Pending/Confirmed/Cancelled
    payment_status = db.Column(db.String(20), default='Unpaid')    # Unpaid/Paid/Refunded
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)


# ─── PRESCRIPTION ─────────────────────────────────────────────────────────────
class Prescription(db.Model):
    __tablename__ = 'prescription'
    id             = db.Column(db.Integer, primary_key=True)
    doctor_id      = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_id     = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    treatment_name = db.Column(db.String(200))
    medicine       = db.Column(db.Text)
    advice         = db.Column(db.Text)
    remark         = db.Column(db.Text)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    patient = db.relationship('Patient', backref='prescriptions', lazy=True)


# ─── BILL ─────────────────────────────────────────────────────────────────────
class Bill(db.Model):
    __tablename__ = 'bill'
    id             = db.Column(db.Integer, primary_key=True)
    bill_no        = db.Column(db.String(20), unique=True, nullable=False)
    patient_id     = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
    amount         = db.Column(db.Float)
    date           = db.Column(db.String(20))
    time           = db.Column(db.String(20))
    status         = db.Column(db.String(20), default='Paid')  # Paid/Refunded
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    appointment = db.relationship('Appointment', backref='bill', lazy=True)


# ─── LOGIN MANAGER LOADER ─────────────────────────────────────────────────────
@login_manager.user_loader
def load_user(user_id):
    if user_id.startswith('patient_'):
        return Patient.query.get(int(user_id.split('_')[1]))
    elif user_id.startswith('doctor_'):
        return Doctor.query.get(int(user_id.split('_')[1]))
    elif user_id.startswith('admin_'):
        return Admin.query.get(int(user_id.split('_')[1]))
    return None
