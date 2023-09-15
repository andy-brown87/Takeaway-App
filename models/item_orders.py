from app import db

class Item_order(db.Model):
    __tablename__ = "item orders"

    id = db.Column(db.Integer, primary_key=True) 
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer())

    def __repr__(self):
        return f"<Order: {self.id}: {self.quantity}>"