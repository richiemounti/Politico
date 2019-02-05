from flask import request, Blueprint, make_response, jsonify
from app.api.v1.models.election_models import PartyModels
import json
p_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

class Party():
    @p_v1.route('/parties', methods=['POST'])
    def create_party():
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']

        response = PartyModels().create_party(name, hqAddress, logoUrl)

        return make_response(jsonify({
            "msg": "party created succefully"
    }))         

   
    