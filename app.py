from flask import Flask, request, render_template

app = Flask(__name__)


item_list = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = 'World'

    return render_template('name_form.html', name=name)


@app.route('/grocery-list', methods=['GET'])
def grocery_list():
    if request.method == 'POST':
        item = request.form['item']
        amount = request.form['amount']
        item_list.append((item, amount))
    return render_template('grocery_list.html', items=item_list)


@app.route('/add-item', methods=['POST'])
def add_item():
    item = request.form['item']
    amount = request.form['amount']
    item_list.append((item, amount))

    if item_list:
        response = 'Your list:'
    else:
        response = ''
    response += '<ul>'
    for item, amount in item_list:
        response += f'<li>{item} : {amount}</li>'
    response += '</ul>'
    return response


if __name__ == '__main__':
    app.run()
