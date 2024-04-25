from flask import Flask, request, jsonify
from fetch_order import fetch_orders
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route("/get_orders")
def get_orders():
    orders = fetch_orders()
    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True, port=9406) 
