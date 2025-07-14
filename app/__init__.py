from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from faker import Faker
import random
from utils.interest_options import INTEREST_OPTIONS

db = SQLAlchemy()
fake = Faker()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)

    with app.app_context():
        from .models import User, Shortlist
        db.create_all()

        if User.query.first() is None:
            print("🌱 Seeding mock data...")
            seed_mock_users()

    from .user_routes import user_bp
    from .match_routes import matches_bp
    from .shortlist_routes import shortlist_bp

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(matches_bp, url_prefix='/matches')
    app.register_blueprint(shortlist_bp, url_prefix='/shortlist')

    return app

def seed_mock_users():
    from .models import User

    base_interests = ["Travel", "Gym", "Cooking", "Writing"]

    bhuvan = User(
        name="Bhuvan Verma",
        age=25,
        interests=base_interests,
        bio="qwertyuioplkjhgfdsaz",
        profile_picture="https://i.pravatar.cc/150?img=12"
    )
    db.session.add(bhuvan)

    for _ in range(5):
        name = fake.unique.first_name()
        age = random.randint(20, 40)
        interests = random.sample(base_interests, 3)
        bio = fake.sentence(nb_words=10)
        profile_picture = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"
        db.session.add(User(
            name=name,
            age=age,
            interests=interests,
            bio=bio,
            profile_picture=profile_picture
        ))

    for _ in range(95):
        name = fake.unique.first_name()
        age = random.randint(18, 50)
        interests = random.sample(INTEREST_OPTIONS, random.randint(3, 6))
        bio = fake.sentence(nb_words=10)
        profile_picture = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"
        db.session.add(User(
            name=name,
            age=age,
            interests=interests,
            bio=bio,
            profile_picture=profile_picture
        ))

    db.session.commit()
    print("✅ Seeded 100 users including Bhuvan Verma")
