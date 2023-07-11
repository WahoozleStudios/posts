from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
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
    
if __name__ == '__main__':
    app.run(host="86.170.72.128")

