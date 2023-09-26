from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from models.order import Order
from app import db


new_order_blueprint = Blueprint("new order", __name__)
# this controller function should just be inside a 'item_orders_controller' file, as it's code that's related to handling a request about saving a new 'item_order' 


@new_order_blueprint.route("/orders/<int:order_id>/add_item", methods=["POST"])
def get_new_order(order_id):
    item_to_add = request.form["item_id"]
    quantity_to_add = request.form["quantity"]
    item_order_to_be_saved = Item_order(item_id=item_to_add, quantity=quantity_to_add, order_id=order_id )
    db.session.add(item_order_to_be_saved)
    db.session.commit()
    return redirect(f"/orders/{order_id}")
    
    