# H1 PYTHON PROJECT

## H2 Food Takeaway

---

I have been tasked with making an order management system for a takeaway. 
This takeaway takes orders over the phone and enters them into the system for the kitchen to cook and keep track of them. 

The app is able to create a customer with a name, phone number, address, and a list of orders.

A customer is able to place several orders. The orders contain a list of item's. The item's have a name and a price.

---

To use the app you will need:

 Python3 and postgresql installed on your machine,

 ---

** You will also need the following pip3 packages: 
`pip3 install flask`
`pip3 install flask-SWLAlchemy`
`pip3 install flask-migrate`
`pip3 install python-dotenv`

---

** You will need to set up a database using the following command in terminal:
`create db itemOrders_app`

---

** On line 8:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://__________@localhost:5432/ItemOrders_app"
 you will need to enter your username after postgresql://
 and before @localhost:5432/ItemOrders_app"

 ---

** To populate the database you will need to run the following commands in terminal:
`flask db upgrade
`flask seed`

---

** To run the application use the following command in terminal:
`flask run`

---

** Copy the http link and paste into the chrome browser.