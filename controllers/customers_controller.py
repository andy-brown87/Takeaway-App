from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
from app import db 


customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def get_customers():
    items_from_db = Item.query.all()
    customers_from_db = Customer.query.all()
    return render_template("customer/customer.jinja", customers=customers_from_db, items=items_from_db)

@customers_blueprint.route("/customers", methods=["GET"])
def new_customer():
    customers_from_db = Customer.query.all()
    # We are not using our "customers" in our 'new_customer.jinja' template, so it's redundant to pass this in. We only should pass data into our templates that we plan on using. 
    return render_template("customer/new_customer.jinja", customers=customers_from_db #)



# @customers_blueprint.route("/customers/delete", methods =["POST"])
# def delete_customer():
#     id = int(request.form.get("customer_id"))
#     customers_from_db = Customer.query.all()
#     for customer in customers_from_db:
#         if customer.id == id:
#             db.session.delete(customer)
#             db.session.commit()
#     return render_template("index.jinja")

