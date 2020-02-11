import models
from flask import Blueprint


bands = Blueprint('bands', 'bands')

@bands.route('/')
def bands_index():
	return 'bands resource working!'