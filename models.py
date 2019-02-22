from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
app=Flask(__name__)
db=SQLAlchemy(app)
migrate=migrate(app,db)

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    mobile=db.Column(db.Integer(10),unique=True)
    email=db.Column(db.String(120),unique=True)
    password=db.Column(db.String(20),unique=True)

def add_user():
    nu=user()

