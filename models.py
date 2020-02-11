from peewee import *

DATABASE = SqliteDatabase('bands.sqlite')

class Band(Model):
	year_formed: IntegerField()
	vocals: CharField()
	guitar: CharField()
	drums: CharField()


	class Meta:
		database = DATABASE

class initialize():
	DATABASE.connect()
	DATABASE.create_tables([Band], safe=True)
	DATABASE.close()