from app import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True) 
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date = db.Column(db.String(64))
    item_orders = db.relationship("Item_order", backref="order")


    def __repr__(self):
        return f"<Order: Id: {self.id}, customer_id: {self.customer_id}, date: {self.date}>"