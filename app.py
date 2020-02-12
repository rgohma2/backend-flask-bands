# print('Hello, world!')

from flask import Flask, g

from flask_cors import CORS

from resources.bands import bands

import models

DEBUG=True
PORT=8000


app = Flask(__name__)

CORS(bands, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(bands, url_prefix='/api/v1/bands')

@app.before_request
def before_request():
	"""Connect to the database before each request"""
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	"""Close the database after each request"""
	g.db.close()
	return response


@app.route('/')
def index():
	return 'Welcome to the Bands App'


















if __name__ == '__main__': 
	app.run(debug=DEBUG, port=PORT)