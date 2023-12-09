from flask import Flask, render_template
from flask_socketio import SocketIO,join_room,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('home.html')

@socketio.on('connect')
def connect():
    room = 15
    join_room(room)

@socketio.on('user connected')
def streaming(data):
    emit('user connected',data,broadcast=True)

if __name__ == '__main__':
    app.run()
    socketio.run(app)