from flask import Blueprint, request, jsonify, session
from app import db
from app.models.transaction import Transaction
from app.models.listing import Listing
import uuid

transaction_bp = Blueprint('transaction_bp', __name__, url_prefix='/transactions')

# === CREATE TRANSACTION (simulate payment) ===
@transaction_bp.route('/create', methods=['POST'])
def create_transaction():
    data = request.get_json() or {}
    listing_id = data.get('listing_id')
    amount = data.get('amount')
    buyer_id = session.get('user_id') or data.get('buyer_id')  # fallback if not logged in

    if not all([listing_id, buyer_id, amount]):
        return jsonify({"error": "listing_id, buyer_id, and amount are required"}), 400

    new_txn = Transaction(
        id=f"TXN_{uuid.uuid4().hex[:6].upper()}",
        listing_id=listing_id,
        buyer_id=buyer_id,
        amount=float(amount),
        status="pending"
    )

    db.session.add(new_txn)
    db.session.commit()

    return jsonify({
        "message": "Transaction created successfully",
        "transaction_id": new_txn.id,
        "status": new_txn.status
    }), 200


# === UPDATE TRANSACTION STATUS ===
@transaction_bp.route('/update/<txn_id>', methods=['POST'])
def update_transaction(txn_id):
    data = request.get_json() or {}
    new_status = data.get('status', 'success')

    txn = Transaction.query.get(txn_id)
    if not txn:
        return jsonify({"error": "Transaction not found"}), 404

    txn.status = new_status
    db.session.commit()

    return jsonify({"message": f"Transaction marked as {new_status}"}), 200


# === GET SELLER TRANSACTIONS ===
@transaction_bp.route('/seller/<seller_id>', methods=['GET'])
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


# === GET BUYER TRANSACTIONS ===
@transaction_bp.route('/buyer/<buyer_id>', methods=['GET'])
def get_buyer_transactions(buyer_id):
    transactions = Transaction.query.filter_by(buyer_id=buyer_id).all()
    return jsonify([
        {
            "transaction_id": t.id,
            "listing_id": t.listing_id,
            "amount": t.amount,
            "status": t.status
        } for t in transactions
    ])
