from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the PROGIDY_CS_04 Project!</h1><p>This is a demo web app for Render deployment.</p>"