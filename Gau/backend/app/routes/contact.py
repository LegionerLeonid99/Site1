from flask import Blueprint, request, jsonify, current_app
from flask_mail import Message
from app import mail
from app.services.email_service import EmailService
import re

contact_bp = Blueprint('contact', __name__)
email_service = EmailService()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_required_fields(data, required_fields):
    missing_fields = []
    for field in required_fields:
        if field not in data or not data[field].strip():
            missing_fields.append(field)
    return missing_fields

@contact_bp.route('/contact', methods=['POST'])
def general_contact():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'service', 'message']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        # Send email
        result = email_service.send_contact_email(
            name=data['name'],
            email=data['email'],
            service=data['service'],
            message=data['message']
        )
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you for your inquiry! We will contact you soon.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500

@contact_bp.route('/contact/appliances', methods=['POST'])
def appliance_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone', 'appliance', 'brand', 'issue', 'message']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        result = email_service.send_appliance_service_email(data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you! We will contact you soon about your appliance repair.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Appliance contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500

@contact_bp.route('/contact/coffee-machines', methods=['POST'])
def coffee_machine_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone', 'machineType', 'brand', 'issue']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        result = email_service.send_coffee_machine_service_email(data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you! We will contact you soon about your coffee machine repair.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Coffee machine contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500

# Add similar endpoints for other service types
@contact_bp.route('/contact/dishwashers', methods=['POST'])
def dishwasher_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone', 'dishwasherType', 'brand', 'issue', 'message']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        result = email_service.send_dishwasher_service_email(data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you! We will contact you soon about your dishwasher repair.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Dishwasher contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500

@contact_bp.route('/contact/washing-machines', methods=['POST'])
def washing_machine_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone', 'washerType', 'brand', 'issue', 'message']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        result = email_service.send_washing_machine_service_email(data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you! We will contact you soon about your washing machine repair.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Washing machine contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500

@contact_bp.route('/contact/commercial-equipment', methods=['POST'])
def commercial_equipment_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone', 'businessType', 'equipmentType', 'brand', 'issue', 'urgency']
        missing_fields = validate_required_fields(data, required_fields)
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        result = email_service.send_commercial_equipment_service_email(data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Thank you! We will contact you soon about your commercial equipment repair.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send message. Please try again.'
            }), 500
            
    except Exception as e:
        current_app.logger.error(f'Commercial equipment contact form error: {str(e)}')
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }), 500
