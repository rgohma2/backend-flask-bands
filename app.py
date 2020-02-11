# print('Hello, world!')

from flask import Flask 

from resources.bands import bands

import models

DEBUG=True
PORT=8000


app = Flask(__name__)

app.register_blueprint(bands, url_prefix='/api/v1/bands')




@app.route('/')
def index():
	return 'Welcome to the Bands App'


















if __name__ == '__main__': 
	app.run(debug=DEBUG, port=PORT)