from app import db
from models.user import User
from models.listing import Listing
from models.transaction import Transaction
from datetime import datetime, timedelta

# Drop old data if any
db.drop_all()
db.create_all()

# Create seller (Ojash)
seller = User(
    full_name="Ojash Anand",
    email="ojash@gmail.com",
    phone="9999999999",
    role="seller"
)
seller.set_password("ojash123")

# Create renter
renter = User(
    full_name="Ravi Kumar",
    email="ravi@gmail.com",
    phone="8888888888",
    role="renter"
)
renter.set_password("ravi123")

# Add both users to DB
db.session.add(seller)
db.session.add(renter)
db.session.commit()

# Create Netflix listing for Ojash
listing = Listing(
    service_name="Netflix",
    plan_type="Premium",
    price=200,
    available_days=7,
    account_email="netflix.ojash@gmail.com",
    account_password="abcd1234",
    description="Netflix Premium plan available for 7 days",
    seller_id=seller.id
)
db.session.add(listing)
db.session.commit()

# Simulate transaction (Ravi rents Ojash’s Netflix)
transaction = Transaction(
    listing_id=listing.id,
    buyer_id=renter.id,
    seller_id=seller.id,
    amount=200,
    rented_from=datetime.now(),
    rented_to=datetime.now() + timedelta(days=7),
    status="completed"
)
db.session.add(transaction)
db.session.commit()

print("✅ Example data added successfully!")
