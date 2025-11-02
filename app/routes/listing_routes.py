from flask import Blueprint, jsonify
from app.models.listing import Listing

listing_bp = Blueprint('listing_bp', __name__)

# 🟢 Route to get all listings
@listing_bp.route('/listings', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    return jsonify([
        {
            "id": l.id,
            "name": l.name,
            "description": l.description,
            "price": l.price,
            "validity_days": l.validity_days,
            "user_id": l.user_id
        } for l in listings
    ])

# 🟢 Route to get listings by a specific seller
@listing_bp.route('/seller/<string:seller_id>/listings', methods=['GET'])
def get_listings_by_seller(seller_id):
    listings = Listing.query.filter_by(user_id=seller_id).all()
    if not listings:
        return jsonify({"message": f"No listings found for seller {seller_id}"}), 404
    return jsonify([
        {
            "id": l.id,
            "name": l.name,
            "description": l.description,
            "price": l.price,
            "validity_days": l.validity_days
        } for l in listings
    ])
