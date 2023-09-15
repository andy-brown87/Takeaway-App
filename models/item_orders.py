from app import db

class Item_order(db.Model):
    __tablename__ = "item orders"

    id = db.Column(db.Integer, primary_key=True) 
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer())

    def __repr__(self):
        return f"<Item_order: Id:{self.id}, order_id: {self.order_id}, item_id: {self.item_id}, quantity: {self.quantity}>"