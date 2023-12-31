from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from models.order import Order
from app import db

new_customer_blueprint = Blueprint("new customer", __name__)

@new_customer_blueprint.route("/customer/new_customer", methods = ["POST"])
def save_customer():
    name_to_add = request.form["name"]
    phone_to_add = request.form["phone_number"]
    address_to_add = request.form["address"]
    customer_to_be_saved = Customer(name = name_to_add, phone_number= phone_to_add, address = address_to_add,)
    db.session.add(customer_to_be_saved)
    db.session.commit()
    return render_template("/customer/new_customer.jinja")

@new_customer_blueprint.route("/customer/new_customer", methods = ["GET"])
def add_new_customer():
    return render_template("/customer/new_customer.jinja")