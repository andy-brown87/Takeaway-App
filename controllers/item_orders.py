from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from models.order import Order
from app import db

item_order_blueprint = Blueprint("item order", __name__)
# this should live in the 'orders_controller'file as it's a function that's handling a request about a 'order'
@item_order_blueprint.route("/orders/<int:order_id>")
def add_items(order_id):
    items_to_add = Item.query.all()
    order_to_add = Order.query.get(order_id)
    price_to_add = Item.query.all()
    return render_template("item_orders/item_orders.jinja", items=items_to_add, order=order_to_add, price=price_to_add,)

    
