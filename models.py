from peewee import *

from flask_login import UserMixin

DATABASE = SqliteDatabase('bands.sqlite')

class User(Model, UserMixin):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()


	class Meta:
		database = DATABASE

class Band(Model):
	year_formed = IntegerField()
	name = CharField()
	vocals = ForeignKeyField(User, backref='bands')
	guitar = CharField()
	drums = CharField()


	class Meta:
		database = DATABASE

class initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Band], safe=True)
	DATABASE.close()

