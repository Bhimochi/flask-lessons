from flask import Flask, request

app = Flask(__name__)

# Home page route
@app.route('/')
# Route handler
def index():
    return '<h3>Hello World!</h3>'

@app.route('/hello/<string:spam>')
def hello(spam):
    return {'message': f'Hello {spam}!'}

@app.route('/add/<int:num1>/<int:num2>')
def add(num1:int, num2:int):
    try:
        x = num1
        y = num2
        return {'result': x + y}
    except TypeError:
        return {'error': 'num1 and num2 must be integers'}, 400

@app.route('/foo/')
def foo():
    person = {'name': 'John', 'age': 21}
    return ['Matt', 50, 3.14159]

@app.errorhandler(404)
def not_found(e):
    return {'error': 'Not implemented!'}, 501

if __name__ == '__main__':
    app.run(debug=True)
