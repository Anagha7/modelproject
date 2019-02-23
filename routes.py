from app import app
from flask import render_template


@app.route('/')
def chat():
    return render_template('chats1.html')

@app.route('/chat')
def chattem():
    return render_template('chattem.html')


@app.route('/login')
def login(username,password):

    return render_template('login.html')

@app.route('/register')
def reg(name,birtday,gender,email,phone,password):
    print(os.path.realpath(os.path.dirname('vendor')))
    db = connect_db()
    db.execute('INSERT INTO user VALUES(name,birtday,gender,email,phone,password)')
    return render_template('register.html')
