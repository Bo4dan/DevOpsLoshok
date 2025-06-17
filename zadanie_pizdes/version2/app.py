# version2/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1 style="color:blue">Version 2</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
