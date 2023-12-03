from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

class Home:
    def __init__(self):
        self.message = "Welcome to the Home page!"

@app.get("/home")
def get_home():
    home = Home()
    return {"message": home.message}

@app.get("/teams")
def read_teams():
    try:
        # Connexion à la base de données
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="database",
            port="5432",
        )
        cursor = conn.cursor()

        cursor.execute("SELECT player_name FROM stats;")
        teams = cursor.fetchall()

        cursor.close()
        conn.close()

        return {"teams": [team[0] for team in teams]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to the database: {e}")

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"},
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
