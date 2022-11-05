import socketio


sio = socketio.Server()
app = socketio.ASGIApp(sio)


@sio.event
def connect(sid, environ):
    print(sid, "connected")


@sio.event
def disconnect(sid, environ):
    print(sid, "disconnected")
