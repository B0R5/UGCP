from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = "super_secret_key"  # Klucz do obsługi sesji

# Przykładowe dane
operations = [
    {"operation_name": "Zbieranie surowców", "operation_description": "Zbieraj surowce z okolicy", "creation_date": "2025-02-05"},
    {"operation_name": "Budowa fabryki", "operation_description": "Zbuduj nową fabrykę w bazie", "creation_date": "2025-02-05"}
]

agents = [
    {"name": "Jan", "surname": "Kowalski"},
    {"name": "Anna", "surname": "Nowak"}
]

buildings = [
    {"building_name": "Fabryka", "quantity": 5},
    {"building_name": "Magazyn", "quantity": 2}
]

resources = [
    {"resource_name": "Drewno", "resource_amount": 100},
    {"resource_name": "Kamień", "resource_amount": 50},
    {"resource_name": "Żelazo", "resource_amount": 30},
    {"resource_name": "Złoto", "resource_amount": 10},
    {"resource_name": "Woda", "resource_amount": 200},
    {"resource_name": "Zboże", "resource_amount": 150}
]

# Strona główna (dashboard gracza)
@app.route('/')
def home():
    if not session.get("user"):
        return redirect(url_for("login"))

    user_name = session.get("user")
    user_full_name = "John Doe"  # Tu możesz ustawić prawdziwe imię i nazwisko użytkownika

    return render_template(
        "index.html", 
        user=user_name, 
        user_full_name=user_full_name,
        operations=operations, 
        agents=agents, 
        buildings=buildings, 
        resources=resources
    )

# Logowanie użytkownika
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        USERS = {
            "user_1": "secure_password",
            "player_2": "password123",
            "guest": "guestpass"
        }
        
        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password")
    
    return render_template('auth/login.html')

# Wylogowanie użytkownika
@app.route('/auth/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
