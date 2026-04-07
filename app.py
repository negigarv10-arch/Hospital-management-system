from flask import Flask
from config import Config
from extensions import db, login_manager
from routes.auth import auth_bp
from routes.patient import patient_bp
from routes.doctor import doctor_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.select_login'

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp, url_prefix='/patient')
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(admin_bp, url_prefix='/admin')


    
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


















  