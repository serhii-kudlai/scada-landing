"""
URL routes for the landing contact-form backend (Flask Blueprint).
"""
from flask import Blueprint
from views import contact_send, health

bp = Blueprint('api', __name__, url_prefix='/api')

bp.add_url_rule('/health', view_func=health, methods=['GET'])
bp.add_url_rule('/contact/send/', view_func=contact_send, methods=['POST', 'OPTIONS'])
