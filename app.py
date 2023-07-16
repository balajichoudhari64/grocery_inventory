from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
inventory = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory', methods=['GET', 'POST'])
def handle_inventory():
    if request.method == 'GET':
        return jsonify(inventory)
    elif request.method == 'POST':
        data = request.get_json()
        if data:
            inventory.append(data)
            return jsonify({'message': 'Item added to inventory'})
        else:
            return jsonify({'message': 'Invalid data'})

if __name__ == '__main__':
    app.run(debug=True)
