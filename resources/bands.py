import models
from flask import Blueprint, request


bands = Blueprint('bands', 'bands')

@bands.route('/', methods=['GET'])
def bands_index():
	return 'bands resource working!'

@bands.route('/', methods=['POST'])
def create_band():
	payload = request.get_json()
	band = models.Bands.create(year_formed=payload['year_formed'], vocals=payload['vocals'], guitar=payload['guitar'], drums=payload['drums'])
	print(band)