from flask import current_app
from flask_mail import Message
from app import mail
from datetime import datetime

class EmailService:
    def send_contact_email(self, name, email, service, message):
        try:
            # Email to business
            business_msg = Message(
                subject=f'New Contact Form Submission - {service}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Service:</strong> {service}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            # Confirmation email to customer
            customer_msg = Message(
                subject=f'Thank you for contacting {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[email]
            )
            
            customer_msg.html = f"""
            <h2>Thank you for your inquiry!</h2>
            <p>Dear {name},</p>
            <p>Thank you for contacting {current_app.config["BUSINESS_NAME"]}. We have received your message about <strong>{service}</strong> and will get back to you within 24 hours.</p>
            <p><strong>Your message:</strong></p>
            <p>{message}</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team<br>
            {current_app.config["BUSINESS_PHONE"]}</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Email sending error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_appliance_service_email(self, data):
        try:
            # Email to business
            business_msg = Message(
                subject=f'New Appliance Repair Request - {data["appliance"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>New Appliance Repair Request</h2>
            <p><strong>Customer:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Appliance:</strong> {data['appliance']}</p>
            <p><strong>Brand:</strong> {data['brand']}</p>
            <p><strong>Issue:</strong> {data['issue']}</p>
            <p><strong>Details:</strong></p>
            <p>{data['message']}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            # Confirmation email to customer
            customer_msg = Message(
                subject=f'Appliance Repair Request Received - {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            
            customer_msg.html = f"""
            <h2>Your Appliance Repair Request</h2>
            <p>Dear {data['name']},</p>
            <p>We have received your repair request for your <strong>{data['brand']} {data['appliance']}</strong>.</p>
            <p><strong>Issue reported:</strong> {data['issue']}</p>
            <p>Our expert technicians will contact you within 24 hours to schedule a convenient service appointment.</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team<br>
            {current_app.config["BUSINESS_PHONE"]}</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Appliance service email error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_coffee_machine_service_email(self, data):
        try:
            # Email to business
            business_msg = Message(
                subject=f'New Coffee Machine Repair Request - {data["machineType"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]            )
            
            business_msg.html = f"""
            <h2>New Coffee Machine Repair Request</h2>
            <p><strong>Customer:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Machine Type:</strong> {data['machineType']}</p>
            <p><strong>Brand:</strong> {data['brand']}</p>
            {f"<p><strong>Model:</strong> {data['model']}</p>" if data.get('model') else ""}
            <p><strong>Issue:</strong> {data['issue']}</p>
            <p><strong>Details:</strong></p>
            <p>{data.get('message', 'No additional details provided')}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            # Confirmation email to customer
            customer_msg = Message(
                subject=f'Coffee Machine Repair Request Received - {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            
            customer_msg.html = f"""
            <h2>Your Coffee Machine Repair Request</h2>
            <p>Dear {data['name']},</p>
            <p>We have received your repair request for your <strong>{data['brand']} {data['machineType']}</strong>.</p>
            <p><strong>Issue reported:</strong> {data['issue']}</p>
            <p>Our coffee machine specialists will contact you within 24 hours to get your daily brew back on track!</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team<br>
            {current_app.config["BUSINESS_PHONE"]}</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Coffee machine service email error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_dishwasher_service_email(self, data):
        try:
            business_msg = Message(
                subject=f'New Dishwasher Repair Request - {data["dishwasherType"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>New Dishwasher Repair Request</h2>
            <p><strong>Customer:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Dishwasher Type:</strong> {data['dishwasherType']}</p>
            <p><strong>Brand:</strong> {data['brand']}</p>
            <p><strong>Issue:</strong> {data['issue']}</p>
            <p><strong>Details:</strong></p>
            <p>{data['message']}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            customer_msg = Message(
                subject=f'Dishwasher Repair Request Received - {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            
            customer_msg.html = f"""
            <h2>Your Dishwasher Repair Request</h2>
            <p>Dear {data['name']},</p>
            <p>We have received your repair request for your <strong>{data['brand']} {data['dishwasherType']}</strong>.</p>
            <p>Our dishwasher experts will contact you within 24 hours to schedule your repair.</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Dishwasher service email error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_washing_machine_service_email(self, data):
        try:
            business_msg = Message(
                subject=f'New Washing Machine Repair Request - {data["washerType"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>New Washing Machine Repair Request</h2>
            <p><strong>Customer:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Washer Type:</strong> {data['washerType']}</p>
            <p><strong>Brand:</strong> {data['brand']}</p>
            <p><strong>Issue:</strong> {data['issue']}</p>
            <p><strong>Details:</strong></p>
            <p>{data['message']}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            customer_msg = Message(
                subject=f'Washing Machine Repair Request Received - {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            
            customer_msg.html = f"""
            <h2>Your Washing Machine Repair Request</h2>
            <p>Dear {data['name']},</p>
            <p>We have received your repair request for your <strong>{data['brand']} {data['washerType']}</strong>.</p>
            <p>Our washing machine specialists will contact you within 24 hours.</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Washing machine service email error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_commercial_equipment_service_email(self, data):
        try:
            urgency_flag = "🚨 URGENT" if data.get('urgency') in ['urgent', 'emergency'] else ""
            
            business_msg = Message(
                subject=f'{urgency_flag} Commercial Equipment Repair - {data["equipmentType"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>{urgency_flag} Commercial Equipment Repair Request</h2>
            <p><strong>Business:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Business Type:</strong> {data['businessType']}</p>
            <p><strong>Equipment:</strong> {data['equipmentType']}</p>
            <p><strong>Brand:</strong> {data['brand']}</p>
            <p><strong>Urgency:</strong> {data['urgency']}</p>
            <p><strong>Issue:</strong> {data['issue']}</p>
            <p><strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            customer_msg = Message(
                subject=f'Commercial Equipment Repair Request Received - {current_app.config["BUSINESS_NAME"]}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data['email']]
            )
            
            customer_msg.html = f"""
            <h2>Your Commercial Equipment Repair Request</h2>
            <p>Dear {data['name']},</p>
            <p>We have received your repair request for your <strong>{data['brand']} {data['equipmentType']}</strong>.</p>
            <p><strong>Urgency Level:</strong> {data['urgency']}</p>
            <p>Our commercial equipment specialists understand the importance of keeping your business running. We will contact you immediately to minimize downtime.</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Commercial Team</p>
            """
            
            mail.send(business_msg)
            mail.send(customer_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Commercial equipment service email error: {str(e)}')
            return {'success': False, 'error': str(e)}
    
    def send_newsletter_signup(self, email):
        try:
            # Welcome email to subscriber
            welcome_msg = Message(
                subject=f'Welcome to {current_app.config["BUSINESS_NAME"]} Newsletter!',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[email]
            )
            
            welcome_msg.html = f"""
            <h2>Welcome to {current_app.config["BUSINESS_NAME"]}!</h2>
            <p>Thank you for subscribing to our newsletter.</p>
            <p>You'll receive:</p>
            <ul>
                <li>Appliance maintenance tips</li>
                <li>Special service offers</li>
                <li>Seasonal appliance care guides</li>
                <li>Latest repair techniques and advice</li>
            </ul>
            <p>We respect your privacy and will never share your email address.</p>
            <br>
            <p>Best regards,<br>
            {current_app.config["BUSINESS_NAME"]} Team</p>
            """
            
            # Notification to business
            business_msg = Message(
                subject=f'New Newsletter Subscription',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )
            
            business_msg.html = f"""
            <h2>New Newsletter Subscription</h2>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Subscribed:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """
            
            mail.send(welcome_msg)
            mail.send(business_msg)
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Newsletter signup email error: {str(e)}')
            return {'success': False, 'error': str(e)}
