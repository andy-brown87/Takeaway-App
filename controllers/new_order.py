from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.item_orders import Item_order
from models.customer import Customer
from app import db


new_order_blueprint = Blueprint("new order", __name__)



