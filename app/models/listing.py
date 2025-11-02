from app import db
import uuid


class Listing(db.Model):
    __tablename__ = 'listing'

    id = db.Column(
        db.String(50),
        primary_key=True,
        default=lambda: f"LIST_{uuid.uuid4().hex[:8].upper()}"
    )
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    validity_days = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)

    # Optional soft delete flag (uncomment if you want to support hiding listings instead of deleting)
    # is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Listing {self.name}>"

    def to_dict(self):
        """Helper method to serialize listing objects easily"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "validity_days": self.validity_days,
            "user_id": self.user_id,
            # "is_active": self.is_active,
        }

