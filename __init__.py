from  flask import Flask,render_template,request
from flask_socketio import SocketIO,send,emit
app=Flask(__name__)
app.config['SECRET_KEY']="mysecretkey"
#from app import routes

sock=SocketIO(app)

contacts ={'Asha':['online','hi',''],
           'Raghu':['online','hello',''],
           'Aparna' :['offline','see you',''],
           'Dev':['offline' ,'bye',''],
           'Ammu' :['online','good night','']
           }

users = []

@sock.on('message')
def handle_message(msg):

    print('message : '+msg)
    sock.send(msg,broadcast=True)
    sesid=request.sid
    users.append(sesid)
    print(users)
   # sock.emit('inboxchat',users)



@sock.on('usermessage',namespace='/private')
def private_message(msg):
    print('private message : '+msg)
    emit('new pvt message',msg,room=users[1])

@sock.on('username',namespace='/private')
def rcv_username(user):

    users.append({user:request.sid})
    print(users)
   # emit('fromflask',msg,broadcast=True)

@app.route('/')
def chat():
    return render_template('chattem.html')

@app.route('/chat')
def chattem():
    return render_template('chattem.html')

if __name__ == "__main__" :
    sock.run(app,debug='true')
