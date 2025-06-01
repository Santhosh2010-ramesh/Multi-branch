from flask import Blueprint, request, jsonify

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin':
        return jsonify({"message": "Login Success"}), 200
    return jsonify({"message": "Login Failed"}), 401
