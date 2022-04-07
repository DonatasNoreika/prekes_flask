from flask_wtf import FlaskForm
from wtforms import (StringField,
                     IntegerField,
                     SubmitField,
                     SelectField,
                     FloatField)
from wtforms.validators import (DataRequired,
                                Email,
                                InputRequired)
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from .models import (Customer,
                     Status)


class CustomerForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    lastname = StringField('Lastname', [DataRequired()])
    email = StringField('Email', [])
    submit = SubmitField('Submit')


class ProductForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    price = FloatField('Price', [])
    submit = SubmitField('Submit')

def get_pk(obj):
    return str(obj)

def customer_query():
    return Customer.query

def status_query():
    return Status.query

class OrderForm(FlaskForm):
    customer = QuerySelectField(query_factory=customer_query, get_label="lastname", get_pk=get_pk)
    status = QuerySelectField(query_factory=status_query, get_label="name", get_pk=get_pk)
    submit = SubmitField('Submit')
