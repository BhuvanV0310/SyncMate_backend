# seed_data.py
import random
from faker import Faker
from app import create_app
from app.models import db, User
from utils.interest_options import INTEREST_OPTIONS

fake = Faker()

def generate_mock_users(n=100):
    all_users = []

    base_interests = ["Travel", "Gym", "Cooking", "Writing"]  # Your profile's interests

    # First create 5 guaranteed matching users
    for _ in range(5):
        name = fake.unique.first_name()
        age = random.randint(20, 40)
        interests = random.sample(base_interests, 3)  # Guaranteed 3 shared
        bio = fake.sentence(nb_words=10)
        profile_picture = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"

        user = User(
            name=name,
            age=age,
            interests=interests,
            bio=bio,
            profile_picture=profile_picture
        )
        all_users.append(user)

    # Now generate the rest randomly
    for _ in range(n - 5):
        name = fake.unique.first_name()
        age = random.randint(18, 50)
        interests = random.sample(INTEREST_OPTIONS, k=random.randint(3, 6))
        bio = fake.sentence(nb_words=10)
        profile_picture = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"

        user = User(
            name=name,
            age=age,
            interests=interests,
            bio=bio,
            profile_picture=profile_picture
        )
        all_users.append(user)

    return all_users


def seed_database():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        users = generate_mock_users(100)

        for user in users:
            db.session.add(user)

        db.session.commit()
        print("✅ Mock users created!")

if __name__ == "__main__":
    seed_database()
