from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
from app import db 




order_blueprint = Blueprint("orders", __name__)

# @order_blueprint.route('/order')
# def index():
#     return render_template('index.jinja', title='Jurassic Pork', orders = orders)


# @order_blueprint.route("/orders",  methods=['GET'])
# def create_order():
#     date = request.form['date']
#     order = Order(customer_id = customer_id, date = date)
#     db.session.add(order)
#     db.session.commit()
#     return redirect('/orders')




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

@order_blueprint.route("/orders", methods=["POST"])
def save_order():
    order_item = request.form["item"]
    order_quantity = request.form["quantity"]
    customer_id = request.form["customers"]
    order_to_be_saved = Item_order(order_item=order_item, order_quantity=order_quantity, customer_id=customer_id)

    db.session.add(order_to_be_saved)
    db.session.commit()
    return redirect(f"/orders/{order_to_be_saved}")