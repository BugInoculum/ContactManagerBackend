from flask import Flask
from flask_cors import CORS
from .contact.apis.contact import contacts_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(contacts_api, url_prefix='/api')
    CORS(app)
    return app
