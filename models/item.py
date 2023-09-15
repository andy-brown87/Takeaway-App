from app import db

class Item(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True) 
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer())

    def __repr__(self):
        return f"<Order: {self.id}: {self.quantity}>"