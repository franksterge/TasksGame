from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

socketio = SocketIO()
def crate_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    CORS(app)
    socketio.init_app(app)
    return app