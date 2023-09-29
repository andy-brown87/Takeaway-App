from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://andrewbrown@localhost:5432/ItemOrders_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.customers_controller import customers_blueprint
from controllers.orders_controller import order_blueprint
from controllers.items_controller import items_blueprint
from controllers.item_orders import new_order_blueprint
from controllers.new_customer_controller import new_customer_blueprint


app.register_blueprint(customers_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(new_order_blueprint)
app.register_blueprint(new_customer_blueprint)


migrate = Migrate(app, db)

@app.route("/")
def home():
    return "This is the home page for Jurassic Pork!"

