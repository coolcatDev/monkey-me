import os

class BaseConfig(object): 
	SECRET_KEY = "kjdsbfkjgdf78sft"
	UPLOAD_FOLDER = 'static/uploads'

	# LOCAL
	# SQLALCHEMY_DATABASE_URI= 'sqlite:///monkeyDB.db'

	# Heroku
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
