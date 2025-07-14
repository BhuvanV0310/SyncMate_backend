# app/routes.py

from flask import Blueprint, jsonify
from .models import User
from sqlalchemy import func

routes = Blueprint("routes", __name__)

@routes.route("/matches/<string:username>", methods=["GET"])
def get_matches(username):
    # Get the current user
    current_user = User.query.filter(func.lower(User.name) == func.lower(username)).first()

    if not current_user:
        return jsonify([]), 404

    current_interests = set(current_user.interests)

    # Get all other users
    other_users = User.query.filter(User.name != username).all()

    matches = []
    for user in other_users:
        shared_interests = current_interests.intersection(user.interests)
        if len(shared_interests) >= 2:
            matches.append({
                "name": user.name,
                "age": user.age,
                "interests": user.interests,
                "shared_interests": list(shared_interests),
                "bio": getattr(user, "bio", ""),
                "profile_picture": getattr(user, "profile_picture", ""),
            })

    return jsonify(matches)
