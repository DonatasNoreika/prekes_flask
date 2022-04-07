from shop import app, db
from flask import render_template, redirect, url_for
from .models import (Customer,
                     MyOrder,
                     Product,
                     OrderLine)
from .forms import (CustomerForm,
                    ProductForm,
                    OrderForm,
                    LineForm)


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


@app.route('/new_product', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('new_product.html', form=form)


@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(name=form.name.data, lastname=form.lastname.data, email=form.email.data)
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('customers'))
    return render_template('new_customer.html', form=form)


@app.route('/new_order', methods=['GET', 'POST'])
def new_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = MyOrder(customer=form.customer.data, status=form.status.data)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('orders'))
    return render_template('new_order.html', form=form)


@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))


@app.route('/add_line/<int:id>', methods=['GET', 'POST'])
def add_line(id):
    form = LineForm()
    order = MyOrder.query.get(id)
    if form.validate_on_submit():
        print("Labas")
        line = OrderLine(product=form.product.data, qty=form.qty.data)
        order.lines.append(line)
        db.session.commit()
        return redirect(url_for('orders'))
    return render_template('add_line.html', form=form)
