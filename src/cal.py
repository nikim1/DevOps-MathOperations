from flask import Flask

app = Flask(__name__)


@app.route('/add/<int:first>/<int:second>', methods=['GET'])
def add(first, second):
    return str(first + second)


@app.route('/subtract/<int:first>/<int:second>', methods=['GET'])
def subtract(first, second):
    return str(first - second)


@app.route('/multiply/<int:first>/<int:second>', methods=['GET'])
def multiply(first, second):
    return str(first * second)


@app.route('/divide/<int:first>/<int:second>', methods=['GET'])
def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return str(first/second)


@app.route('/', methods=['GET'])
def hello():
    return "Welcome to Math Calculator!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
