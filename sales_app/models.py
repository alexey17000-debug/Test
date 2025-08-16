from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100), nullable=False)
    Price = db.Column(db.Numeric(10, 2), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)

class Customer(db.Model):
    __tablename__ = 'customers'
    CustomerID = db.Column(db.Integer, primary_key=True)
    CustomerName = db.Column(db.String(100), nullable=False)
    ContactEmail = db.Column(db.String(100))
    PhoneNumber = db.Column(db.String(15))

class Sale(db.Model):
    __tablename__ = 'sales'
    SaleID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('products.ProductID'))
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'))
    SaleDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    QuantitySold = db.Column(db.Integer, nullable=False)
    TotalAmount = db.Column(db.Numeric(10, 2), nullable=False)