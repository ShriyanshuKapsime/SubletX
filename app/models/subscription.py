from app import db
from datetime import datetime, timedelta

class Subscription(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    listing_id = db.Column(db.String(50), db.ForeignKey('listing.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default="active")

    def __init__(self, id, user_id, listing_id, validity_days):
        self.id = id
        self.user_id = user_id
        self.listing_id = listing_id
        self.start_date = datetime.utcnow()
        self.end_date = self.start_date + timedelta(days=validity_days)
