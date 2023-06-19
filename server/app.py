from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from consolidations import get_consolidations

# Configure App
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'


# Route for getting consolidations
@app.route("/", methods=['POST'])
@cross_origin()
def fetch_consolidations():
    try:
        data = request.json
        consolidations = get_consolidations(data['location'])
        return jsonify(consolidations)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})