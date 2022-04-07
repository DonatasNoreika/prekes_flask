from shop import app
from flask import render_template
from .models import (Customer,
                     MyOrder,
                     Product)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers')
def customers():
    return render_template('customers.html', customers=Customer.query.all())


@app.route('/orders')
def orders():
    return render_template('orders.html', orders=MyOrder.query.all())


@app.route('/products')
def products():
    return render_template('products.html', products=Product.query.all())
