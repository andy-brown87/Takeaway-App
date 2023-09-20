from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    address = db.Column(db.String(64))
    orders = db.relationship("Order", backref="customer")

    def __repr__(self):
        return f"<Customer: Id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, address: {self.address}>"