from flask import Blueprint, request, jsonify
from . import db
from .models import Shortlist

shortlist_bp = Blueprint('shortlist', __name__)

@shortlist_bp.route('', methods=['POST'])
def add_to_shortlist():
    data = request.get_json()
    username = data.get('username')
    match_id = data.get('match_id')

    if not username or match_id is None:
        return jsonify({'error': 'Invalid data'}), 400

    entry = Shortlist(username=username, match_id=match_id)
    db.session.add(entry)
    db.session.commit()

    return jsonify({'message': 'Added to shortlist'}), 201

@shortlist_bp.route('/<username>', methods=['GET'])
def get_shortlist(username):
    matches = Shortlist.query.filter_by(username=username).all()
    return jsonify([{'match_id': s.match_id} for s in matches])
