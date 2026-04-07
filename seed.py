"""
Run this ONCE after first launch to create the default admin account
and some sample doctors.

Usage:
    python seed.py
"""
from app import create_app
from extensions import db
from models import Admin, Doctor

app = create_app()

with app.app_context():
    db.create_all()

    # ── Default Admin ──────────────────────────────────────
    if not Admin.query.filter_by(a_id='ADMIN001').first():
        admin = Admin(
            a_id   = 'ADMIN001',
            name   = 'Hospital Admin',
            gender = 'Male',
            email  = 'admin@moeka.org',
            mobile = '9999999999',
        )
        admin.set_password('admin123')
        db.session.add(admin)
        print("✅ Admin created  — ID: ADMIN001  Password: admin123")

    # ── Sample Doctors ─────────────────────────────────────
    doctors = [
        dict(d_id='DOC001', name='Akansha Rathi',  age=35, gender='Female',
             specialization='ENT Specialist',    experience='18 years',
             language='English, Hindi, Urdu',
             mobile='8945639342', email='akansha@moeka.org',
             schedule='Mon 9AM-12PM, Wed 2PM-4PM, Fri 12PM-3PM',
             consultant_fee=600, password='doc123'),

        dict(d_id='DOC002', name='Shikha Bisht',   age=42, gender='Female',
             specialization='Plastic Surgeon',   experience='15 years',
             language='English, Hindi',
             mobile='8945639343', email='shikha@moeka.org',
             schedule='Tue 10AM-1PM, Thu 3PM-6PM',
             consultant_fee=1200, password='doc123'),

        dict(d_id='DOC003', name='Reha Karmakar',  age=38, gender='Female',
             specialization='Pediatrician',      experience='12 years',
             language='English, Bengali, Hindi',
             mobile='8945639344', email='reha@moeka.org',
             schedule='Mon-Fri 9AM-11AM',
             consultant_fee=500, password='doc123'),

        dict(d_id='DOC004', name='Muskan Gupta',   age=31, gender='Female',
             specialization='Ophthalmologist',   experience='7 years',
             language='English, Hindi',
             mobile='8945639345', email='muskan@moeka.org',
             schedule='Wed 11AM-2PM, Sat 9AM-12PM',
             consultant_fee=700, password='doc123'),

        dict(d_id='DOC005', name='Kavita Pandey',  age=45, gender='Female',
             specialization='Psychiatrist',      experience='20 years',
             language='English, Hindi',
             mobile='8945639346', email='kavita@moeka.org',
             schedule='Mon 2PM-5PM, Thu 10AM-1PM',
             consultant_fee=900, password='doc123'),

        dict(d_id='DOC006', name='Ashi Singh',     age=50, gender='Female',
             specialization='Cardiologist',      experience='25 years',
             language='English, Hindi',
             mobile='8945639347', email='ashi@moeka.org',
             schedule='Tue 9AM-12PM, Fri 2PM-5PM',
             consultant_fee=1500, password='doc123'),
    ]

    for d in doctors:
        if not Doctor.query.filter_by(d_id=d['d_id']).first():
            pw = d.pop('password')
            doc = Doctor(**d)
            doc.set_password(pw)
            db.session.add(doc)
            print(f"✅ Doctor created  — ID: {d['d_id']}  Name: {d['name']}")

    db.session.commit()
    print("\n🎉 Done! You can now run:  python app.py")
    print("   Admin Login  → ID: ADMIN001  | Password: admin123")
    print("   Doctor Login → ID: DOC001    | Password: doc123")
