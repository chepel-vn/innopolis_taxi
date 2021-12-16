import db
from flask import Flask, render_template, request
app = Flask(__name__)

server_url = "/api/v1/"

@app.route('/')
def my_fn():
    return 'my first web application'

@app.route(f"{server_url}orders", methods = ['GET', 'POST'])
def orders():
    if request.method == 'POST':
        address_from = request.form.get('from')
        address_to = request.form["to"]
        db.add_order(1, 1, address_from, address_to)
        return render_template('index.html')
    else:
        return render_template('orders.html')


if __name__ == '__main__':
    # db.fill_init_db()
    app.run(host='127.0.0.1', port=5050)
