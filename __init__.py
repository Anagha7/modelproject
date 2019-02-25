from  flask import Flask,render_template,request
from flask_socketio import SocketIO,send,emit
app=Flask(__name__)
app.config['SECRET_KEY']="mysecretkey"
#from app import routes

sock=SocketIO(app)

@sock.on('message')
def handle_message(msg):

    print('message : '+msg)
    sock.send(msg,broadcast=True)

@sock.on('usermessage',namespace='/public')
def public_message(msg):
    print('public message : '+msg)
    emit('fromflask',msg,broadcast=True)

@sock.on('username',namespace='/private')
def rcv_username(user):
    print(user+request.sid)
   # emit('fromflask',msg,broadcast=True)

@app.route('/')
def chat():

    return render_template('chat2.html')

@app.route('/chat')
def chattem():
    return render_template('chattem.html')

if __name__ == "__main__" :
    sock.run(app,debug='true')
