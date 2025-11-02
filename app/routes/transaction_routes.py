from flask import Blueprint, jsonify
from app.models.transaction import Transaction
from app.models.listing import Listing

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/seller/<seller_id>/transactions', methods=['GET'])
def get_seller_transactions(seller_id):
    transactions = Transaction.query.join(Listing).filter(Listing.user_id == seller_id).all()
    return jsonify([
        {
            "transaction_id": t.id,
            "listing_id": t.listing_id,
            "buyer_id": t.buyer_id,
            "amount": t.amount,
            "status": t.status
        } for t in transactions
    ])
