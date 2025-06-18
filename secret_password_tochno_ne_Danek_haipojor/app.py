from flask import Flask, request
import os

app = Flask(__name__)
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

@app.route('/')
def index():
    pwd = request.args.get("password")
    if pwd:
        if pwd == ADMIN_PASSWORD:
            return '<body style="background-color: lightgreen">Добро пожаловать, администратор!</body>'
        else:
            return '<body style="background-color: lightcoral">Неверный пароль!</body>'
    return '<body>Введите пароль в параметре URL.</body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
