import models
from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

bands = Blueprint('bands', 'bands')

@bands.route('/', methods=['GET'])
def bands_index():
	all_bands_query = models.Band.select()
	band_dicts = [model_to_dict(b) for b in all_bands_query]
	
	return jsonify(
			data=band_dicts,
			message=f'sucessfully retireved {len(band_dicts)} bands',
			status=200
		), 200



@bands.route('/', methods=['POST'])
def create_band():
	payload = request.get_json()
	print('payload >> ',payload)
	band = models.Band.create(year_formed=payload['year_formed'], name=payload['name'], vocals=payload['vocals'], guitar=payload['guitar'], drums=payload['drums'])
	print(band)

	band_dict=model_to_dict(band)

	return(jsonify(data=band_dict, status={'message': 'sucessfully created a band'})), 201