from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


class FoodOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    items = db.relationship('Item', secondary='order_item', lazy='subquery',
                            backref=db.backref('orders', lazy=True))
    time = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='pending')
    total_price = db.Column(db.Float, nullable=False, default=0.0)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price
