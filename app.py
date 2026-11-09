import sqlite3
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = Path(__file__).parent / "instance" / "votes.db"
CAR_BRANDS = [
    "Toyota",
    "Lexus",
    "Ford",
    "Honda",
    "Chevrolet",
    "Nissan",
    "BMW",
    "Alfa Romeo",
    "Ferrari",
    "Lamborghini",
    "Pagani",
    "Mclaren",
    "Tesla",
]


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    DATABASE.parent.mkdir(exist_ok=True)

    connection = get_db_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


create_table()


@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/form1nico', methods=['GET', 'POST'])
def formpage():
    selected_brand = None
    error = None

    if request.method == 'POST':
        selected_brand = request.form.get('brand')

        if selected_brand not in CAR_BRANDS:
            error = "Please choose one of the car brands."
            selected_brand = None
        else:
            connection = get_db_connection()
            connection.execute(
                "INSERT INTO votes (brand) VALUES (?)",
                (selected_brand,),
            )
            connection.commit()
            connection.close()

    return render_template(
        'form1nico.html',
        brands=CAR_BRANDS,
        selected_brand=selected_brand,
        error=error,
    )


@app.route('/admin')
def admin_page():
    connection = get_db_connection()
    votes = connection.execute(
        """
        SELECT brand, COUNT(*) AS vote_count
        FROM votes
        GROUP BY brand
        ORDER BY vote_count DESC, brand
        """
    ).fetchall()
    total_votes = connection.execute(
        "SELECT COUNT(*) FROM votes"
    ).fetchone()[0]
    connection.close()

    return render_template(
        'admin.html',
        votes=votes,
        total_votes=total_votes,
    )
