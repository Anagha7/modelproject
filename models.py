from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
app=Flask(__name__)
db=SQLAlchemy(app)
migrate=migrate(app,db)

class user(db.Model):
    uid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    birthday=db.Column(db.DateTime)
    gender=db.Column(db.String(1))
    mobile=db.Column(db.Integer(10),unique=True)
    email=db.Column(db.String(120),unique=True)
    password=db.Column(db.String(20),unique=True)

def register():
    nu=user()
