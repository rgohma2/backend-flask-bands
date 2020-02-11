import models
from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

bands = Blueprint('bands', 'bands')

@bands.route('/', methods=['GET'])
def bands_index():
	return 'bands resource working!'



@bands.route('/', methods=['POST'])
def create_band():
	payload = request.get_json()
	print('payload >> ',payload)
	band = models.Band.create(year_formed=payload['year_formed'], vocals=payload['vocals'], guitar=payload['guitar'], drums=payload['drums'])
	print(band)

	band_dict=model_to_dict(band)

	return(jsonify(data=band_dict, status={'message': 'sucessfully created a band'})), 201