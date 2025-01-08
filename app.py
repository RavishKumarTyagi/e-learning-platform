from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "your_secret_key_here"

# Dummy data for users (this would normally come from a database)
users = {}

# Sample course data with image references
courses = [
    {"name": "Python for Beginners", "description": "Learn Python from scratch", "image": "course1.jpg"},
    {"name": "Advanced JavaScript", "description": "Master JavaScript", "image": "course2.jpg"},
    {"name": "Machine Learning", "description": "Learn how to build ML models", "image": "course3.jpg"},
    {"name": "Data Science", "description": "Become a Data Science expert", "image": "course4.jpg"},
    {"name": "Web Development", "description": "Build full-stack web applications", "image": "course5.jpg"},
    {"name": "Digital Marketing", "description": "Learn the basics of Digital Marketing", "image": "course6.jpg"},
    {"name": "Blockchain Basics", "description": "Introduction to Blockchain technology", "image": "course7.jpg"},
    {"name": "DevOps Essentials", "description": "Understand DevOps practices", "image": "course8.jpg"},
    {"name": "Cyber Security", "description": "Learn to secure networks and systems", "image": "course9.jpg"},
    {"name": "Artificial Intelligence", "description": "Discover the world of AI", "image": "course10.jpg"}
]

# Route for homepage
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', courses=courses)
    return redirect(url_for('login'))

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and the password matches
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid username or password.", 403
    return render_template('login.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match", 400

        # Store the hashed password
        if username not in users:
            users[username] = {'password': generate_password_hash(password)}
            return redirect(url_for('login'))
        else:
            return "Username already exists", 400

    return render_template('register.html')

# Route to logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
