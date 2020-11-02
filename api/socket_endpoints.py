from application import socketio
from flask_socketio import send, emit

@socketio.on('json')
def handle_json(json):
    send(json, json=True, broadcast=True)


