from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def base():
    with app.app_context():
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/home')
def homeRedirect():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()