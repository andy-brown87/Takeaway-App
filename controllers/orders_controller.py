from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
from app import db 


order_blueprint = Blueprint("orders", __name__)



@order_blueprint.route('/order')
def index():
    return render_template('index.html', title='Jurassic Pork', orders = Order)