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
    # db.drop_all()
    
    # item1 = Item(items_name="Original Hotdog", items_price="6.50")
    # item2 = Item(items_name="Vegetarian Hotdog", items_price="6.00")

    # db.session.add(item1)
    # db.session.add(item2)

    # db.session.commit()

    # customer1 = Customer(name="Barry Eadie", phone="0131332445", address="56 Polwarth Gardens", customer_id = customer1.id)
    # customer2 = Customer(name="Angus Cook", phone="0131338665", address="26 Smith Street", customer_id = customer2.id)

    # db.session.add(customer1)
    # db.session.add(customer2)

    # db.session.commit()
    
    items_from_db = Item.query.all()
    customers_from_db = Customer.query.all()

    return render_template("index.jinja", customers=customers_from_db, items=items_from_db)

@customers_blueprint.route("/customers/delete", methods =["POST"])
def delete_customer():
    id = int(request.form.get("customer_id"))
    customers_from_db = Customer.query.all()
    for customer in customers_from_db:
        if customer.id == id:
            db.session.delete(customer)
            db.session.commit()
    return render_template("index.jinja")

