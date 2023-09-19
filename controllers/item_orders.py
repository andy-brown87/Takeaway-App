from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from models.order import Order
from app import db

item_order_blueprint = Blueprint("item order", __name__)

@item_order_blueprint.route("/orders/<int:order_id>")
def add_items():
    item_to_add = Item_order.query.all()
    order_to_add = Order.query.all()
    return render_template("items/items.jinja", item_to_add=item_to_add, order_to_add=order_to_add)

    
