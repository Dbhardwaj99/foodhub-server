from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but helps with performance
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    orders = db.relationship('FoodOrder', backref='customer', lazy=True)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)  # Make name required
    address = db.Column(db.String(120))
    opening_time = db.Column(db.Time)
    closing_time = db.Column(db.Time)
    items = db.relationship('Item', backref='restaurant', lazy=True)
    photo = db.Column(db.LargeBinary)  # For storing image data


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo = db.Column(db.LargeBinary)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)


class FoodOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(120))  # Could be a list of items
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
