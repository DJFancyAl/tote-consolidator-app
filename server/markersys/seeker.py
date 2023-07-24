from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from database_sql import search_gmc, search_color

bp = Blueprint("seeker", __name__, url_prefix="/seeker")

# Find totes by GMC
@bp.route("/<gmc>")
@cross_origin()
def get_gmc(gmc):
    try:
        location = request.args.get("location")
        results = search_gmc(gmc, location)
        totes = sorted(results, key = lambda x: float(x['weight']))
        if(totes == []):
            return jsonify({"error": "No totes found!"})
        return jsonify(totes)
    except Exception as e:
        return jsonify({"error": "Not found. Try another search."})

# Find totes by Size and Color
@bp.route("/<color>/<size>")
@cross_origin()
def get_ing(color, size):
    try:
        location = request.args.get("location")
        results = search_color(color.upper(), size.upper(), location)
        totes = sorted(results, key = lambda x: float(x['weight']))
        if(totes == []):
            return jsonify({"error": "No totes found!"})
        return jsonify(totes)
    except Exception as e:
        return jsonify({"error": "Not found. Try another search."})