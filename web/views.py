from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sendMessage', methods=['POST'])
def send_message():
    message = request.form['message']
    print(message)
    return message, 200


if __name__ == "__main__":
    app.run()
