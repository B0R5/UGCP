from flask import render_template
from flask_login import login_required, current_user
from app.database.models import User

@app.route("/dashboard")
@login_required  # Używamy dekoratora, aby tylko zalogowani użytkownicy mieli dostęp
def dashboard():
    # Tu możesz dodać dodatkowe informacje o użytkowniku, jeśli chcesz
    return render_template("dashboard.html", user=current_user)
