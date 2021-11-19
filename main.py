from flask import Flask, request, url_for, redirect, render_template

from db_connector import execute_query, connect_to_database

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/customers.html', methods=["GET", "POST"])
def customers():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "SELECT * from Customers;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('customers.html', customer_data=result)

    elif request.method == 'POST':
        email = request.form.get("email")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        address = request.form.get("address")
        zip = request.form.get("zip")
        city = request.form.get("city")
        state = request.form.get("state")
        phone = request.form.get("phone")
        citizenID = request.form.get("citizenID")
        query = """INSERT INTO `Customers` (`customerEmail`, `customerFirstName`, `customerLastName`, `customerAddress`,
                    `customerZip`, `customerCity`, `customerState`, `customerPhone`, `customerCitizenID`) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (email, fname, lname, address, zip, city, state, phone, citizenID)
        execute_query(db_connection, query, data)
        return redirect('customers.html')


@app.route('/orders.html', methods=["GET", "POST"])
def orders():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "SELECT * from Orders;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('orders.html', order_data=result)

    elif request.method == 'POST':
        customerID = request.form.get("customerID")
        orderDate = request.form.get("orderDate")
        query = 'INSERT INTO `Orders` (`customerID`, `orderDate`) VALUES (%s, %s);'
        data = (customerID, orderDate)
        execute_query(db_connection, query, data)
        return redirect('orders.html')


@app.route('/products.html', methods=["GET", "POST"])
def products():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "SELECT * from Products;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('products.html', data=result)

    elif request.method == 'POST':
        productName = request.form.get("name")
        productPrice = request.form.get("price")
        productStock = request.form.get("stock")

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
        productID = request.form.get("productID")
        supplierCompany = request.form.get("company")
        supplierContact = request.form.get("contact")
        supplierAddress = request.form.get("address")
        supplierZip = request.form.get("zip")
        supplierCity = request.form.get("city")
        supplierState = request.form.get("state")
        supplierPhone = request.form.get("phone")
        supplierFax = request.form.get("fax")
        supplierEmail = request.form.get("email")
        supplierURL = request.form.get("url")
        supplierNote = request.form.get("note")

        query = 'INSERT INTO Suppliers (productID, supplierCompany, supplierContact, supplierAddress, supplierZip, supplierCity, supplierState, supplierPhone, supplierFax, supplierEmail, supplierURL, supplierNote) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (productID, supplierCompany, supplierContact, supplierAddress, supplierZip, supplierCity, supplierState,
                supplierPhone, supplierFax, supplierEmail, supplierURL, supplierNote)
        execute_query(db_connection, query, data)
        return redirect('suppliers.html')


if __name__ == "__main__":
    print("Now running on http://127.0.0.1:5000/index.html")
    app.run()
