from flask import Flask
from login import login_bp
from cart import cart_bp
from payment import payment_bp

app = Flask(__name__)

# Register feature routes
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(payment_bp, url_prefix='/payment')

if __name__ == '__main__':
    app.run(debug=True)
