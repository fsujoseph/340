# https://github.com/knightsamar/CS340_starter_flask_app was a huge help in getting this up and working.
# https://canvas.oregonstate.edu/courses/1830239/pages/week-8-learn-using-python-and-flask-framework was another great reference for us.
# Large amounts of code were utilized and inspired from these sources. 

from flask import Flask, request, url_for, redirect, render_template
from db_connector import execute_query, connect_to_database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers.html', methods=["GET", "POST"])
def customers():
    db_connection = connect_to_database()
    if request.method == 'GET':
        queryCustomers = "SELECT * from Customers;"
        customerData = execute_query(db_connection, queryCustomers).fetchall()
        queryCustIds = "SELECT customerID from Customers;"
        customerIds = execute_query(db_connection, queryCustIds).fetchall()
        return render_template('customers.html', customer_data=customerData, list_data=customerIds)

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
        searchCustomerID = request.form.get("searchCustomerID")
        deleteCustomerID = request.form.get("deleteCustomerID")
        data = (email, fname, lname, address, zip, city, state, phone, citizenID)
        if searchCustomerID:
            query = "SELECT * FROM Customers WHERE customerID = %s;"
            customer = execute_query(db_connection, query, searchCustomerID)
            return render_template('customers.html', select_customer=customer)

        elif deleteCustomerID:
            query = "DELETE FROM Customers WHERE customerID = %s;"
            execute_query(db_connection, query, deleteCustomerID)

        elif None not in data:
            query = """INSERT INTO `Customers` (`customerEmail`, `customerFirstName`, `customerLastName`, `customerAddress`,
                                `customerZip`, `customerCity`, `customerState`, `customerPhone`, `customerCitizenID`) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            execute_query(db_connection, query, data)
        return redirect('customers.html')


@app.route('/orders.html', methods=["GET", "POST"])
def orders():
    db_connection = connect_to_database()
    if request.method == 'GET':
        table_query = "SELECT * from Orders;"
        list_query = "SELECT customerID FROM Customers;"
        queryOrderIds = "SELECT orderID FROM Orders;"
        table_result = execute_query(db_connection, table_query)
        list_result = execute_query(db_connection, list_query)
        orderIds = execute_query(db_connection, queryOrderIds)
        return render_template('orders.html', order_data=table_result, list_data=list_result, order_ids=orderIds)

    elif request.method == 'POST':
        customerID = request.form.get("customerID")
        orderDate = request.form.get("orderDate")
        orderID = request.form.get("orderID")
        data = (customerID, orderDate)

        if orderID:
            query = "DELETE FROM Orders WHERE `orderID`=%s;"
            execute_query(db_connection, query, orderID)

        elif None not in data:
            query = 'INSERT INTO `Orders` (`customerID`, `orderDate`) VALUES (%s, %s);'

            execute_query(db_connection, query, data)
        return redirect('orders.html')


@app.route('/products.html', methods=["GET", "POST"])
def products():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "SELECT * from Products;"
        result = execute_query(db_connection, query).fetchall()
        list_query = "SELECT productID from Products;"
        list_result = execute_query(db_connection, list_query).fetchall()
        return render_template('products.html', data=result, list_data=list_result)

    elif request.method == 'POST':
        productName = request.form.get("name")
        productPrice = request.form.get("price")
        productStock = request.form.get("stock")

        productID = request.form.get("productID")
        updateName = request.form.get("updateName")
        updatePrice = request.form.get("updatePrice")
        updateStock = request.form.get("updateStock")

        addProduct = (productName, productPrice, productStock)
        updateProduct = (updateName, updatePrice, updateStock, productID)
        if None not in addProduct:
            query = 'INSERT INTO Products (productName, productPrice, productStock) VALUES (%s,%s,%s)'
            execute_query(db_connection, query, addProduct)

        elif None not in updateProduct:
            query = "UPDATE Products SET productName=%s, productPrice=%s, productStock=%s WHERE productID=%s"
            execute_query(db_connection, query, updateProduct)

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
        if None not in data:
            execute_query(db_connection, query, data)
        return redirect('suppliers.html')

@app.route('/orderitems.html', methods=["GET", "POST"])
def orderItems():
    db_connection = connect_to_database()
    if request.method == 'GET':
        queryAll = "SELECT * from OrderItems;"
        queryOrdIds = "SELECT orderID from Orders;"
        queryProdIds = "SELECT productID from Products;"
        queryOrderItemIds = "SELECT orderItemID from OrderItems;"
        orderItemsData = execute_query(db_connection, queryAll)
        productIds = execute_query(db_connection, queryProdIds)
        orderIds = execute_query(db_connection, queryOrdIds)
        orderItemIds = execute_query(db_connection, queryOrderItemIds)
        return render_template('orderitems.html', order_items=orderItemsData, product_ids=productIds, order_ids=orderIds, order_item_ids=orderItemIds)

    elif request.method == 'POST':
        quantity = request.form.get("quantity")
        productID = request.form.get("productID")
        orderID = request.form.get("orderID")
        orderItemId = request.form.get("orderItemID")
        data = (quantity, productID, orderID)

        if orderItemId:
            query = "DELETE FROM OrderItems WHERE `orderItemID`=%s"
            execute_query(db_connection, query, orderItemId)

        if None not in data:
            query = "INSERT INTO OrderItems (`orderItemQuantity`, `productID`, `orderID`) VALUES (%s, %s, %s);"
            execute_query(db_connection, query, data)

        return redirect('orderitems.html')


if __name__ == "__main__":
    print("Now running on http://127.0.0.1:5000/")
    app.run()