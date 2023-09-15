from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) 
    item_name = db.Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"<Item: Id: {self.id}, item_name: {self.item_name}, price: {self.price}>"