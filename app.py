from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='/var/logs/flask-example.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=False)