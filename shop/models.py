from shop import db
from datetime import datetime


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    lastname = db.Column("Lastname", db.String)
    email = db.Column("Email", db.String)


class Status(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String)


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    price = db.Column("Price", db.Float)


class MyOrder(db.Model):
    __tablename__ = "myorder"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column("Date", db.DateTime, default=datetime.today)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    customer = db.relationship('Customer')
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    status = db.relationship('Status')
    lines = db.relationship('OrderLine')


class OrderLine(db.Model):
    __tablename__ = "orderline"
    id = db.Column(db.Integer, primary_key=True)
    myorder_id = db.Column(db.Integer, db.ForeignKey("myorder.id"))
    myorder = db.relationship('MyOrder')
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    product = db.relationship('Product')
    qty = db.Column("Quantity", db.Integer)
