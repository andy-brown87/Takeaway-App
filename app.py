from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://andrewbrown@localhost:5432/ItemOrders_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.customer import Customer
from models.item import Item
from models.item_orders import Item_order
from models.order import Order

migrate = Migrate(app, db)