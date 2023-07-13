from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/u/zacmoon')
def u_zacmoon():
    return "Zac Moon"
@app.route('/u')
def u():
    return render_template('redirects/u.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run()