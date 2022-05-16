from flask import Flask, render_template,jsonify
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "pswd"

socket_io = SocketIO(app)

@app.route('/')
def hello_world():
    return "hello tester"

@app.route('/chat')
def chatting():
    return render_template('chat.html')

@app.route('/strike')
def strike():
    return render_template('strike.html')

@socket_io.on("message")
def request(message):
    print("message : " + message)
    to_client = dict()
    to_client['message'] = message
    to_client['type'] = 'normal'
    send(to_client, broadcast = True)

if __name__ == '__main__':
    socket_io.run(app,host="0.0.0.0")

