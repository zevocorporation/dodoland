from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from dodolandapp.db import db
from dodolandapp.resources.composeImage import ComposeImage

app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dodoland.db'
db.init_app(app) #instantiating db object...

# with app.app_context():
#     db.create_all()

#Add class to API
api.add_resource(ComposeImage,"/composeimage")


