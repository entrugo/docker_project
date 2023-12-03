from flask import Flask, render_template, requests

app = Flask(__name__)

@app.route("/home")
def index():
    response = requests.get('http://backend:8000/home')
    if response.status_code == 200:
        data = response.json()
        print(data)
        return render_template("index.html",data=data)
    else:
        return "Error retrieving team data"

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/teams")
def teams():
    return render_template("teams.html")
@app.route("/players")
def players():
    return render_template("maintenance.html")
@app.route("/schedule")
def schedules():
    return render_template("maintenance.html")
@app.route("/standings")
def standings():
    return render_template("maintenance.html")
@app.route("/rules")
def rules():
    return render_template("rules.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)