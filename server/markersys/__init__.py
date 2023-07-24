from flask import Flask, request, jsonify, abort
from flask_cors import CORS

def create_app(): 
    # Configure App
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_ORIGINS'] = '*'
    
    from . import consolidator
    from . import seeker
    app.register_blueprint(consolidator.bp)
    app.register_blueprint(seeker.bp)

    return app