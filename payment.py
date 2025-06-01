from flask import Blueprint, request, jsonify

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/process', methods=['POST'])
def process_payment():
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            return jsonify({"message": "Invalid amount"}), 400
        return jsonify({"message": f"Payment of ${amount:.2f} processed"}), 200
    except (ValueError, TypeError):
        return jsonify({"message": "Invalid input"}), 400
