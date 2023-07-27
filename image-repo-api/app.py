from flask import Flask, request, jsonify
import os


# function to load config based on enviroment
def load_config(app):
    env = os.environ.get('FLASK_ENV', 'testing')
    if env == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif env == 'testing':
        app.config.from_object('config.TestingConfig')
    elif env == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        raise ValueError('Invalid FLASK_ENV environment variable entry.')
    
# function to setup database
def setup_db(app):
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    from models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    load_config(app)
    setup_db(app)
    return app

