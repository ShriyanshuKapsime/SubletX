from app import db

class Listing(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    validity_days = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Listing {self.name}>"

