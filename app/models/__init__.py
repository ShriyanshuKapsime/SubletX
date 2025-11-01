# app/models/__init__.py
"""
This file turns 'models' into a Python package.
It also exposes the database object and all models
for easier importing across the app.
"""

from app import db

# Import individual models so they’re registered with SQLAlchemy
from app.models.user import User
from app.models.listing import Listing
from app.models.transaction import Transaction

__all__ = ["db", "User", "Listing", "Transaction"]

