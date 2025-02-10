import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/GRA/database/app.db'  # Ścieżka do bazy danych
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Klucz do sesji (do logowania)
