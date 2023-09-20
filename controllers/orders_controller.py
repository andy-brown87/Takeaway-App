from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
from datetime import datetime
from app import db 


order_blueprint = Blueprint("orders", __name__)


@order_blueprint.route("/customers/<int:id>", methods =["GET"])  
def view_order(id):
    orders_from_db = Order.query.all()
    customers_from_db = Customer.query.all()
    for customers in customers_from_db:
        if customers.id == id:
            return render_template("orders.jinja", order=orders_from_db, customers=customers_from_db)
        

@order_blueprint.route("/orders/delete", methods =["POST"])
def delete_order():
    id = int(request.form.get("order_id"))
    orders_from_db = Order.query.all()
    for order in orders_from_db:
        if order.id == id:
            db.session.delete(order)
            db.session.commit()
    return render_template("orders.jinja", order=orders_from_db)


@order_blueprint.route("/orders/<int:order_id>", methods=["POST"])
def update_order(order_id):
    order_to_update = Order.query.get(order_id)
    order_to_update.item = request.form['item']
    order_to_update.quantity = request.form['quantity']
    db.session.commit()
    return redirect(f"/orders/{order_id}")


# @order_blueprint.route("/orders/<int:order_id>", methods=["GET"])
# def item_order(order_id):
#     item_order=Item.query.get(order_id)
#     order_id=Order.query.get(order_id)
#     return render_template("item_orders/item_orders.jinja", item_order=item_order, order=order_id)

@order_blueprint.route("/orders", methods=["POST"])
def save_order():
    todays_date = datetime.now().strftime("%d/%m/%Y")
    customer_id = request.form["customer_id"]
    order_to_be_saved = Order(customer_id=customer_id, date=todays_date)
    db.session.add(order_to_be_saved)
    db.session.commit()
    return redirect(f"/orders/{order_to_be_saved.id}")

@order_blueprint.route("/orders", methods=["GET"])
def new_order():
    customers_from_db = Customer.query.all()
    return render_template("orders/new_orders.jinja", customers=customers_from_db)

@order_blueprint.route("/orders")
def get_orders():
    order_id_from_db = Item_order.query.all()
    item_id_from_db = Item_order.query.all()
    quantity_from_db = Item_order.query.all()
    return render_template("/orders/new_orders.jinja", order=order_id_from_db, item=item_id_from_db, quantity=quantity_from_db,)

