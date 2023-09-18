from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from app import db


new_order_blueprint = Blueprint("new order", __name__)



@new_order_blueprint.route("/orders/new_order", methods=["GET"])
def new_order():
    item_from_db = Item.query.all()
    order_quantity = order_quantity.query.all()
    customers_id = Customer.id.all()

    return render_template("orders/new_orders.jinja", item=item_from_db, order_quantity=order_quantity, customers_id=customers_id)