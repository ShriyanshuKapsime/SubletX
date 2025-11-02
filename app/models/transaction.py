from app import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    listing_id = db.Column(db.String(50), db.ForeignKey('listing.id'), nullable=False)
    buyer_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    payment_method = db.Column(db.String(20), default="UPI")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    listing = db.relationship('Listing', backref='transactions', lazy=True)
