from flask import Blueprint, jsonify
from app.models import User

matches_bp = Blueprint("matches", __name__)

@matches_bp.route("/<string:username>", methods=["GET"])
def get_matches(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_interests = set(user.interests)
    matches = []

    all_users = User.query.filter(User.name != username).all()
    for other in all_users:
        other_interests = set(other.interests)
        shared = user_interests.intersection(other_interests)

        if len(shared) >= 2:
            match_score = round((len(shared) / len(other_interests)) * 100) if other_interests else 0
            matches.append({
                "id": other.id,
                "name": other.name,
                "age": other.age,
                "interests": other.interests,
                "sharedInterests": list(shared),
                "bio": other.bio,
                "profilePicture": other.profile_picture,
                "matchScore": match_score
            })

    if not matches:
        return jsonify({"message": "No compatible matches found", "matches": []}), 200

    return jsonify(matches)
