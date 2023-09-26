from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.order import Order
from models.item_orders import Item_order

from app import db 

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def get_items():
    items_from_db = Item.query.all()
    order_from_db = Order.query.all() #we are not using this data in the template, `Order.query.all()` returns all the orders from our database so the variable names are innaccurate here. 
    return render_template("/items/items.jinja", items=items_from_db, order=order_from_db,) #we don't need to pass our orders from our database to our '/items/items.jinja'  

