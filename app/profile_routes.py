from flask import Blueprint, request, jsonify
from Backend.app.models import UserProfile
from database import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/api/profile', methods=['POST'])
def create_profile():
    data = request.json
    profile = UserProfile(
        username=data['name'],
        age=data['age'],
        interests=data['interests'],
        bio=data.get('bio'),
        profile_picture=data.get('profilePicture'),
        location=data.get('location')
    )
    db.session.add(profile)
    db.session.commit()
    return jsonify({'message': 'Profile created'}), 201

@profile_bp.route('/api/profile/<username>', methods=['GET'])
def get_profile(username):
    profile = UserProfile.query.filter_by(username=username).first()
    if not profile:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({
        'name': profile.username,
        'age': profile.age,
        'interests': profile.interests,
        'bio': profile.bio,
        'profilePicture': profile.profile_picture,
        'location': profile.location
    })
