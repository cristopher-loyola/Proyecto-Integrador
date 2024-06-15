from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/registro')
def dashboard():
    return render_template('signup.html')

@app.route('/pretest')
def pretest():
    return render_template('pretest.html')

@app.route('/facts')
def curious_facts():
    return render_template('curios')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
