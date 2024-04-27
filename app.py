from flask import Flask, request, jsonify
from func.fetch_order import fetch_orders
from func.update_order import update_order
from func.listitems import fetch_items
from func.create_order import create_order
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route("/get_orders")
def get_orders():
    orders = fetch_orders()
    return jsonify(orders)

@app.route("/get_items")
def get_items():
    orders = fetch_items()
    return jsonify(orders)

@app.route('/create_order', methods=['POST'])
def create_order_endpoint():
    if not request.json:
        return 'Empty request', 400

    print("endpoint accessed!", request.json)
    userName = request.json['user_name']
    orderItems = request.json['order_items']
    total = request.json['total']
    address = request.json['address']
    phone_number = request.json['pNo']
    
    create_order(userName, orderItems, total, address, phone_number)  # Call the function
    # create_order()  # Call the function
    return "Order creation initiated", 200

if __name__ == "__main__":
    app.run(debug=True, port=9406, ssl_context='adhoc') 
