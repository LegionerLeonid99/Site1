from flask import Blueprint, request, jsonify, current_app
from app.services.email_service import EmailService
import re

newsletter_bp = Blueprint('newsletter', __name__)
email_service = EmailService()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@newsletter_bp.route('/newsletter', methods=['POST'])
def newsletter_signup():
    try:
        data = request.get_json()
        
        if not data or 'email' not in data:
            return jsonify({
                'success': False,
                'message': 'Email is required'
            }), 400
        
        email = data['email'].strip()
        
        if not validate_email(email):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        # Send welcome email and notify business
        result = email_service.send_newsletter_signup(email)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you for subscribing to our newsletter!'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to process subscription. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Newsletter signup error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500
