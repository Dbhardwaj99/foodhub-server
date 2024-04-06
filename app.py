from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from models import db, Customer, Restaurant, Item, FoodOrder
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    print("Jingalala huhu")
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_id = data.get('customer_id')
    restaurant_id = data.get('restaurant_id')
    items = data.get('items')

    if not customer_id or not restaurant_id or not items:
        return jsonify({'error': 'Missing required information'}), 400

    total_price = 0
    for item_id in items:
        item = db.session.get(Item, item_id)

        if item:
            total_price += item.price

    # ...

if __name__ == '__main__':
    app.run(debug=True)
