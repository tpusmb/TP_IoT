from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           user_name='TP_IOT',
                           description="Bienvenu dans notre page pour tester le raspbery",
                           blur=False,
                           page_title="index")


@app.route('/sendMessage', methods=['POST'])
def send_message():
    message = request.form['message']
    print(message)
    return message, 200


if __name__ == "__main__":
    app.run()
