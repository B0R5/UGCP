from flask import Flask
from flask_login import LoginManager
from app.database import db
from app.database.models import User
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicjalizacja bazy danych
db.init_app(app)

# Inicjalizacja LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Przekierowanie do strony logowania

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Załadowanie użytkownika z bazy

if __name__ == "__main__":
    app.run(debug=True)
