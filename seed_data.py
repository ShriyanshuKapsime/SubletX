from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="krish", email="krish@example.com")
    user2 = User(username="alice", email="alice@example.com")

    db.session.add_all([user1, user2])
    db.session.commit()

    print("✅ Database seeded!")

