from flask import Blueprint, request, jsonify
from consolidations import get_consolidations
from flask_cors import cross_origin

bp = Blueprint("consolidator", __name__, url_prefix="/consolidator")

# Route for getting consolidations
@bp.route("/", methods=['POST'])
@cross_origin()
def index():
    try:
        data = request.json
        consolidations = get_consolidations(data['location'])
        return jsonify(consolidations)
    except Exception as e:
        return jsonify({"error": str(e)})