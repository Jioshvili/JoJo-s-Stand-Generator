from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random
import requests
import csv
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "bizarre"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('aboutus'))

    return render_template('login.html')


@app.route('/standgenerator')
def standgenerator():
    conn = sqlite3.connect('stands.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT stand_name, stand_user, photo_url FROM photos ORDER BY RANDOM() LIMIT 1')
    photo = cursor.fetchone()

    conn.close()

    return render_template('standgenerator.html', photo=photo)


@app.route("/contactus", methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return 'Thank you for contacting us, ' + name + '! We will get back to you soon.'

    return render_template('contactus.html')


@app.route("/aboutus", methods=['POST', 'GET'])
def aboutus():
    return render_template('aboutus.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    return 'you are logged out'


if __name__ == "__main__":
    app.run(debug=True)