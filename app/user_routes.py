from flask import Blueprint, request, jsonify
from app.models import db, User

user_bp = Blueprint("users", __name__)  # ✅ Define blueprint BEFORE using it

@user_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    interests = data.get("interests")
    bio = data.get("bio")
    profile_picture = data.get("profilePicture")

    if not name or not age or not interests:
        return jsonify({"error": "Missing required fields"}), 400

    existing_user = User.query.filter_by(name=name).first()
    if existing_user:
        return jsonify({
            "message": "User already exists",
            "user": {
                "id": existing_user.id,
                "name": existing_user.name,
                "age": existing_user.age,
                "bio": existing_user.bio,
                "interests": existing_user.interests,
                "profilePicture": existing_user.profile_picture
            }
        }), 200

    user = User(
        name=name,
        age=age,
        interests=interests,
        bio=bio,
        profile_picture=profile_picture
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created",
        "user": {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "bio": user.bio,
            "interests": user.interests,
            "profilePicture": user.profile_picture
        }
    }), 201
