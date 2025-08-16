from flask import Flask, render_template, request, redirect
from models import db, Product, Customer, Sale

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://test:369@LAPTOP-L9MQPQN1/SalesDB?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_sale', methods=['POST'])
def add_sale():
    product_id = request.form['product_id']
    customer_id = request.form['customer_id']
    quantity_sold = request.form['quantity_sold']
    product = Product.query.get(product_id)
    sale = Sale(ProductID=product_id, CustomerID=customer_id,
                QuantitySold=quantity_sold, 
                TotalAmount=product.Price * int(quantity_sold))
    db.session.add(sale)
    db.session.commit()
    return redirect('/')

@app.route('/report')
def report():
    sales = Sale.query.all()
    return render_template('report.html', sales=sales)

if __name__ == '__main__':
    app.run(debug=True)