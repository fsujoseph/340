from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/index.html')
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
    return render_template('products.html')


@app.route('/suppliers.html', methods=["GET", "POST"])
def suppliers():
    return render_template('suppliers.html')


if __name__ == "__main__":
    print("Now running on http://127.0.0.1:5000/index.html")
    app.run()
