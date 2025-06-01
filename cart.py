from flask import Blueprint, request, jsonify

cart_bp = Blueprint('cart', __name__)
cart = []

@cart_bp.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    cart.append(item)
    return jsonify({"message": f"Item added: {item}"}), 200

@cart_bp.route('/', methods=['GET'])
def get_cart():
    return jsonify({"cart": cart}), 200
