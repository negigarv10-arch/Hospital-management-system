import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hms-secret-key-2024')
    # For MySQL: 'mysql+pymysql://user:password@localhost/hms_db'
    # Using SQLite for easy local development
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///hms.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max upload
