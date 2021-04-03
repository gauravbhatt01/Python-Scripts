'''
export flask_app = app.py
flask run
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "hello gaurav"

@app.route("/<name>")
def print_name(name):
	return 'Hi, {}'.format(name)

if __name__ == '__main__':
	app.run(debug = True)