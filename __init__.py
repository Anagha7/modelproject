import os
from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def chat():
    return render_template('chats1.html')

@app.route('/register')
def reg():
    print(os.path.realpath(os.path.dirname('vendor')))
    return render_template('register.html')

if __name__ == "__main__" :
    app.run(debug='true')
