from flask import Blueprint

users_bp = Blueprint('users_bp',__name__)

from app.users import routes
