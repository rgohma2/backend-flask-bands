import models
from flask import Blueprint, request, jsonify

from flask_login import current_user, login_required

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

@bands.route('/<id>', methods=['Delete'])
@login_required
def delete_band(id):
	delete_query = models.Band.delete().where(models.Band.id == id)
	delete_query.execute()
	return jsonify(
		data={}, 
		message=f'sucessfully deleted band with id: {id}',
		status=200
	), 200

@bands.route('/<id>', methods=['PUT'])
@login_required
def update_band(id):
	payload = request.get_json()
	update_query = models.Band.update(**payload).where(models.Band.id == id)
	update_query.execute()

	updated_band = models.Band.get_by_id(id)
	return jsonify(
		data=model_to_dict(updated_band),
		message=f'Successfully updated band at index {id}',
		status=200
	), 200






@bands.route('/', methods=['POST'])
@login_required
def create_band():
	payload = request.get_json()
	payload['vocals'] = current_user.id
	band = models.Band.create(**payload)
	print(band)

	band_dict=model_to_dict(band)
	band_dict['vocals'].pop('password')

	return(jsonify(data=band_dict, status={'message': 'sucessfully created a band'})), 201






