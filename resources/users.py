import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

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

@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		password_good = check_password_hash(user_dict['password'], payload['password'])
		if password_good:
			login_user(user)
			user_dict.pop('password')
			return jsonify(
					data=user_dict,
					message='Sucessfully logged in as {}.'.format(user_dict['email'])
				)
		else:
			print('bad password')
			return jsonify(
				data={},
				message='Email or Password is incorrect',
				status=401
			), 401
	except models.DoesNotExist:
		print('bad username')
		return jsonify(
			data={},
				message='Email or Password is incorrect',
				status=401
			), 401
@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
			data={},
			message='loggout sucessful',
			status=201
		), 201





