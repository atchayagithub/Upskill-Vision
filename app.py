from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3  # Use sqlite3 to run raw SQL commands if needed

app = Flask(__name__)

# Configure the database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database.db')
SQL_FILE_PATH = os.path.join(BASE_DIR, 'script.sql')

# Corrected database URI path (Windows format)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    PhoneNumber = db.Column(db.String(20), nullable=False)
    DateOfBirth = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(100), nullable=False)
    EmailAddress = db.Column(db.String(120), unique=True, nullable=False)
    Education = db.Column(db.String(100), nullable=False)
    CollegeOrOrganization = db.Column(db.String(100), nullable=False)
    PasswordHash = db.Column(db.String(100), nullable=False)  # Note: Hash passwords in production!

# Function to initialize the database from script.sql
def init_db_from_sql():
    if not os.path.exists(DATABASE_PATH):
        print("Database file not found. Initializing database from script.sql...")
        
        # Connect to the SQLite database using sqlite3
        connection = sqlite3.connect(DATABASE_PATH)
        with open(SQL_FILE_PATH, 'r') as sql_file:
            sql_script = sql_file.read()  # Read all SQL commands from the script file
            connection.executescript(sql_script)  # Execute all SQL commands
        connection.close()
        print("Database initialized successfully!")
    else:
        print("Database already exists. Skipping initialization.")

# Routes
@app.route('/')
def login_page():
    return render_template('Loginpage.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        data = request.form
        new_user = User(
            FirstName=data['first_name'],
            LastName=data['last_name'],
            PhoneNumber=data['phone_number'],
            DateOfBirth=data['date_of_birth'],
            Country=data['country'],
            EmailAddress=data['email'],
            Education=data['education'],
            CollegeOrOrganization=data['organization'],
            PasswordHash=data['password']  # Note: Hash passwords in production!
        )
        db.session.add(new_user)
        db.session.commit()
        return "User registered successfully!"
    return render_template('StudentSignUp.html')

if __name__ == '__main__':
    # Initialize the database from the SQL file (if it doesn't already exist)
    init_db_from_sql()
    app.run(debug=True)
