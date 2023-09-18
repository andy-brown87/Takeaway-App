from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from app import db

item_order_blueprint = Blueprint("item order", __name__)

@item_order_blueprint.route("/orders/<int:order_id>", methods=["GET"])
def item_order():
    item_order=Item.query.get(order_id)
    item_id = request.form["item_id"]
    order_id = request.form["order_id"]
    item_quantity = request.form["item_quantity"]
    return render_template("item_order.jinja", item_order=item_order, item_id=item_id, order_id=order_id, item_quantity=item_quantity)