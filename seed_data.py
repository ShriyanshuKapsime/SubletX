from app import create_app, db
from app.models.user import User
from app.models.listing import Listing
from app.models.transaction import Transaction

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- USERS ---
    seller1 = User(username="Anand Kumar", email="anand@example.com", role="seller", phone="9999999999")
    seller1.set_password("pass123")

    seller2 = User(username="Amit Patel", email="amit@example.com", role="seller", phone="8888888888")
    seller2.set_password("pass456")

    seller3 = User(username="Krish Rao", email="krish@example.com", role="seller", phone="7777777777")
    seller3.set_password("pass789")

    renter1 = User(username="Riya Sharma", email="riya@example.com", role="renter", phone="6666666666")
    renter1.set_password("riya123")

    renter2 = User(username="Meryem Ali", email="meryem@example.com", role="renter", phone="5555555555")
    renter2.set_password("meryem123")

    renter3 = User(username="Aditya Verma", email="aditya@example.com", role="renter", phone="4444444444")
    renter3.set_password("aditya123")

    db.session.add_all([seller1, seller2, seller3, renter1, renter2, renter3])
    db.session.commit()  

    # --- LISTINGS ---
    netflix = Listing(
        name="Netflix Premium Account",
        description="Enjoy Netflix Premium for 7 days — 4K streaming, no ads.",
        price=150.0,
        validity_days=7,
        user_id=seller1.id
    )
    spotify = Listing(
        name="Spotify Family Plan",
        description="Ad-free music with Spotify Family access for 5 days.",
        price=50.0,
        validity_days=5,
        user_id=seller2.id
    )
    prime = Listing(
        name="Amazon Prime Video",
        description="Prime Video 4-day pass with HD streaming.",
        price=120.0,
        validity_days=4,
        user_id=seller3.id
    )
    hotstar = Listing(
        name="Disney+ Hotstar",
        description="3-day Hotstar Premium access — IPL, movies, and shows.",
        price=90.0,
        validity_days=3,
        user_id=seller1.id
    )

    db.session.add_all([netflix, spotify, prime, hotstar])
    db.session.commit()  

    # --- TRANSACTIONS ---
    txn1 = Transaction(listing_id=netflix.id, buyer_id=renter1.id, amount=150.0, status="success")
    txn2 = Transaction(listing_id=spotify.id, buyer_id=renter2.id, amount=50.0, status="success")
    txn3 = Transaction(listing_id=prime.id, buyer_id=renter3.id, amount=120.0, status="pending")

    db.session.add_all([txn1, txn2, txn3])
    db.session.commit()

    print("✅ Database seeded successfully with hashed passwords, Users, Listings & Transactions!")



