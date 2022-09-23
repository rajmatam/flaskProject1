from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return 'Welcome back'

@app.route('/multi/<int:num>', methods = ['GET'])
def multiply(num):
    return jsonify({'result': num * 10})


if __name__ == '__main__':
    app.run()
