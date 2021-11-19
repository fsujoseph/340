from flask import Flask, request, url_for, redirect, render_template
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers.html', methods=["GET", "POST"])
def customers():
    email = request.form.get("email")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    address = request.form.get("address")
    zip = request.form.get("zip")
    city = request.form.get("city")
    state = request.form.get("state")
    phone = request.form.get("phone")
    citizenID = request.form.get("citizenID")

    data = []
    if None not in (email, fname, lname, address, zip, city, state, phone, citizenID):
        data = [email, fname, lname, address, zip, city, state, phone, citizenID]

    return render_template('customers.html', data=data)


@app.route('/orders.html', methods=["GET", "POST"])
def orders():
    return render_template('orders.html')


@app.route('/products.html', methods=["GET", "POST"])
def products():
    db_connection = connect_to_database()
    if request.method == 'GET':
      query = "SELECT * from Products;"
      result = execute_query(db_connection, query).fetchall()
      return render_template('products.html', data=result)
    
    elif request.method == 'POST':
      productName= request.form.get("name")
      productPrice= request.form.get("price")
      productStock= request.form.get("stock")
      
      query = 'INSERT INTO Products (productName, productPrice, productStock) VALUES (%s,%s,%s)'
      data = (productName, productPrice, productStock)
      execute_query(db_connection, query, data)
      return redirect('products.html')

@app.route('/suppliers.html', methods=["GET", "POST"])
def suppliers():
    db_connection = connect_to_database()
    if request.method == 'GET':
      query = "SELECT * from Suppliers;"
      result = execute_query(db_connection, query)
      return render_template('suppliers.html', data=result)
      
    elif request.method == 'POST':
      productID= request.form.get("productID")
      supplierCompany= request.form.get("company")
      supplierContact= request.form.get("contact")
      supplierAddress= request.form.get("address")
      supplierZip= request.form.get("zip")
      supplierCity= request.form.get("city")
      supplierState= request.form.get("state")
      supplierPhone= request.form.get("phone")
      supplierFax= request.form.get("fax")
      supplierEmail= request.form.get("email")
      supplierURL= request.form.get("url")
      supplierNote= request.form.get("note")
      
      query = 'INSERT INTO Suppliers (productID, supplierCompany, supplierContact, supplierAddress, supplierZip, supplierCity, supplierState, supplierPhone, supplierFax, supplierEmail, supplierURL, supplierNote) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      data = (productID, supplierCompany, supplierContact, supplierAddress, supplierZip, supplierCity, supplierState, supplierPhone, supplierFax, supplierEmail, supplierURL, supplierNote)
      execute_query(db_connection, query, data)
      return redirect('suppliers.html')

if __name__ == "__main__":
    print("Now running on http://127.0.0.1:5000/index.html")
    app.run()
