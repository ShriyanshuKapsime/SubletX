from app import create_app, db
from app.models.user import User
from app.models.listing import Listing
from app.models.transaction import Transaction

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- USERS ---
    seller1 = User(id="SELLER_ANAND", username="Anand Kumar", email="anand@example.com", role="seller", phone="9999999999")
    seller1.set_password("pass123")

    seller2 = User(id="SELLER_AMIT", username="Amit Patel", email="amit@example.com", role="seller", phone="8888888888")
    seller2.set_password("pass456")

    seller3 = User(id="SELLER_KRISH", username="Krish Rao", email="krish@example.com", role="seller", phone="7777777777")
    seller3.set_password("pass789")

    renter1 = User(id="RENTER_RIYA", username="Riya Sharma", email="riya@example.com", role="renter", phone="6666666666")
    renter1.set_password("riya123")

    renter2 = User(id="RENTER_MERYEM", username="Meryem Ali", email="meryem@example.com", role="renter", phone="5555555555")
    renter2.set_password("meryem123")

    renter3 = User(id="RENTER_ADITYA", username="Aditya Verma", email="aditya@example.com", role="renter", phone="4444444444")
    renter3.set_password("aditya123")

    db.session.add_all([seller1, seller2, seller3, renter1, renter2, renter3])
    db.session.commit()

    # --- LISTINGS ---
    netflix = Listing(
        id="LIST_NETFLIX",
        name="Netflix Premium Account",
        description="Enjoy Netflix Premium for 7 days — 4K streaming, no ads.",
        price=150.0,
        validity_days=7,
        user_id="SELLER_ANAND"
    )

    spotify = Listing(
        id="LIST_SPOTIFY",
        name="Spotify Family Plan",
        description="Ad-free music with Spotify Family access for 5 days.",
        price=50.0,
        validity_days=5,
        user_id="SELLER_AMIT"
    )

    prime = Listing(
        id="LIST_PRIME",
        name="Amazon Prime Video",
        description="Prime Video 4-day pass with HD streaming.",
        price=120.0,
        validity_days=4,
        user_id="SELLER_KRISH"
    )

    hotstar = Listing(
        id="LIST_HOTSTAR",
        name="Disney+ Hotstar",
        description="3-day Hotstar Premium access — IPL, movies, and shows.",
        price=90.0,
        validity_days=3,
        user_id="SELLER_ANAND"
    )

    db.session.add_all([netflix, spotify, prime, hotstar])
    db.session.commit()

    # --- TRANSACTIONS ---
    txn1 = Transaction(id="TXN_001", listing_id="LIST_NETFLIX", buyer_id="RENTER_RIYA", amount=150.0, status="success")
    txn2 = Transaction(id="TXN_002", listing_id="LIST_SPOTIFY", buyer_id="RENTER_MERYEM", amount=50.0, status="success")
    txn3 = Transaction(id="TXN_003", listing_id="LIST_PRIME", buyer_id="RENTER_ADITYA", amount=120.0, status="pending")

    db.session.add_all([txn1, txn2, txn3])
    db.session.commit()

    print("✅ Database seeded successfully with professional readable IDs!")

