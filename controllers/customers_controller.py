from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
from app import db 

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = customers.query.all()
    return render_template("customer/index.jinja", customers = customers)
