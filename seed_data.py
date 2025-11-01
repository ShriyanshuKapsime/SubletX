from app import app
from models import db
from models.user import User
from models.listing import Listing
from models.transaction import Transaction

# Initialize app context
with app.app_context():
    db.drop_all()
    db.create_all()

    # --- USERS ---
    seller1 = User(name="Anand kumar", email="anand@gmail.com", password="hashed123", role="seller", phone="9999999999")
    seller2 = User(name="Amit Patel", email="amit@gmail.com", password="hashed789", role="seller", phone= "5555555555")
    seller3 = User(name="krish rao", email="krish@gmail.com", password="hashed789", role="seller", phone= "5555555566")
    seller4 = User(name="sudhanshu", email="sudhanshu@gmail.com", password="hashed789", role="seller", phone= "5555555556")
    seller5 = User(name="riya rao", email="riyarao@gmail.com", password="hashed789", role="seller", phone= "5555555577")
    seller6 = User(name="meryem", email="meryem@gmail.com", password="hashed789", role="seller", phone= "888888888855")
    # renter1 = User(name="Riya Singh", email="riya@gmail.com", password="hashed456", role="renter", phone="8888888888")
    # renter2 = User(name="jason", email="jason@gmail.com", password="hashed456", role="renter", phone="88888844")
    # renter3 = User(name="shivam", email="shivam@gmail.com", password="hashed456", role="renter", phone="85548888")
    # renter4 = User(name="aryan", email="aryan@gmail.com", password="hashed456", role="renter", phone="888455888")
    # renter5 = User(name="sanya", email="sanya@gmail.com", password="hashed456", role="renter", phone="84668888")
    # renter6 = User(name="kajal", email="kajal@gmail.com", password="hashed456", role="renter", phone="88564588")
    # renter7 = User(name="kriti", email="kriti@gmail.com", password="hashed456", role="renter", phone="8857845948")
    # renter8 = User(name="kartik", email="kartik@gmail.com", password="hashed456", role="renter", phone="88865847555")
    
    
    
    
    
    
    db.session.add_all([seller1, seller2, seller3, seller4, seller5, seller6, renter1,renter2,renter3,renter4,renter5,renter6, renter7,renter8])
    db.session.commit()

    # --- LISTINGS ---
    netflix = Listing(
        service_name="Netflix",
        email="netflix_meryem@gmail.com",
        password="net123",
        price=150.0,
        validity_days=7,
        description="Netflix Premium account for 1 week.",
        user_id=seller6.id
    )

    spotify = Listing(
        service_name="Spotify",
        email="amit_spotify@gmail.com",
        password="spo456",
        price=50.0,
        validity_days=5,
        description="Spotify Family plan access for 5 days.",
        user_id=seller2.id
    )
    
    amazon_prime = Listing(
        service_name="Amazon Prime",
        email="riya_prime@gmail.com",
        password="spo456",
        price=150.0,
        validity_days=4,
        description="Amazon Prime Family plan access for 5 days.",
        user_id=seller5.id
    )
    
    hotstar = Listing(
        service_name="Hotstar",
        email="anand_hotstar@gmail.com",
        password="spo456",
        price=200.0,
        validity_days=4,
        description="Hotstar Family plan access for 5 days.",
        user_id=seller1.id
    )
    

    db.session.add_all([netflix, spotify, amazon_prime])
    db.session.commit()

    # --- TRANSACTIONS ---
    txn1 = Transaction(listing_id=netflix.id, buyer_id=renter1.id, amount=150.0, status="success")

    db.session.add(txn1)
    db.session.commit()

    print("✅ Seed data added successfully!")
