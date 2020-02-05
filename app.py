from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sendMsg', methods=['POST'])
def add_income():
    request.get_json()
    return '', 204


if __name__ == '__main__':
    app.run()
