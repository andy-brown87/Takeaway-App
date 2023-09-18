from app import db
from models.customer import Customer
from models.item_orders import Item_order
from models.item import Item
from models.order import Order
import click 

from flask.cli import with_appcontext

@click.command(name="seed")
@with_appcontext
def seed():
    
    item1 = Item(name="The OG Dog", price=6.50)
    item2 = Item(name="The Scotty Dog", price=7.50)
    item3 = Item(name="The Chihuahua", price=8.00)

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)

    customer1 = Customer(name="Barry Eadie", phone_number="0131653875", address="35 Smith Street")
    customer2 = Customer(name="Angus Cook", phone_number="01698776554", address="10 hewlett Way")
    customer3 = Customer(name="Sophie Jones", phone_number="07549765142", address="16 Polwarth Gardens")

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)

    db.session.commit()
