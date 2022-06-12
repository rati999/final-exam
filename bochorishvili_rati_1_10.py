from flask import Flask
from flask_sqlalchemy import SQLAlchemy, model

app = Flask(_name_)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flower.db'

class Flower(model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False)
    color = db.Column(db.String(length=20), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

if _name_ == "_main_":
    app.run(host='5.5.5.5')