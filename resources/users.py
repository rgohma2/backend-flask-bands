import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user

from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

# @users.route('/')
# def test():
# 	return 'it works'

@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:
		models.User.get(models.User.email == payload['email'])

		return jsonify(
				data={},
				message='A user with that email already exists',
				status=401
			), 401

	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		createdUser = models.User.create(**payload)

		login_user(createdUser)

		user_dict = model_to_dict(createdUser)
		user_dict.pop('password')

		return jsonify(
				data=user_dict,
				message='Sucessfully registered as {}'.format(user_dict['email']),
				status=201
			), 201



