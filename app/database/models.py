from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)  # Przechowywanie hasza hasła
    inventory = db.relationship('Item', backref='owner', lazy=True)
    buildings = db.relationship('Building', backref='owner', lazy=True)

    def set_password(self, password):
        """Haszowanie hasła przed zapisaniem do bazy danych"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Sprawdzanie poprawności hasła"""
        return check_password_hash(self.password_hash, password)
