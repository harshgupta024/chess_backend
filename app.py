from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game_logic import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('game_state', game.get_state())

@socketio.on('move')
def handle_move(data):
    move = data['move']
    result = game.make_move(move)
    emit('game_state', game.get_state())
    emit('move_result', result)

if __name__ == '__main__':
    socketio.run(app, debug=True)
