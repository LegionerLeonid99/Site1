from flask import current_app
from flask_mail import Message
from app import mail
from datetime import datetime

class EmailService:
    def send_contact_email(self, name, email, service, message):
                try:
                        business_msg = Message(
                                subject=f'Osaco Website Contact - {service}',
                                sender=current_app.config['MAIL_USERNAME'],
                                recipients=[current_app.config['BUSINESS_EMAIL']]
                        )

                        business_msg.html = f"""
                        <h2>New Website Enquiry (Osaco)</h2>
                        <p><strong>From:</strong> {name} &lt;{email}&gt;</p>
                        <p><strong>Service Selected:</strong> {service}</p>
                        <hr style='margin:16px 0;'>
                        <p style='margin:0 0 4px 0;'><strong>Message:</strong></p>
                        <p style='white-space:pre-line;margin-top:4px'>{message}</p>
                        <hr style='margin:16px 0;'>
                        <p style='font-size:12px;color:#555'>Submitted {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (server time)</p>
                        """

                        customer_msg = Message(
                                subject=f'Osaco – We received your {service} enquiry',
                                sender=current_app.config['MAIL_USERNAME'],
                                recipients=[email]
                        )

                        customer_msg.html = f"""
                        <h2 style='margin:0 0 12px 0;'>Thank you – your enquiry is with our team</h2>
                        <p style='margin:0 0 12px 0;'>Hi {name},</p>
                        <p style='margin:0 0 12px 0;'>We’ve received your request regarding <strong>{service}</strong>. An Osaco technician will review the details and contact you (usually within 1 business hour during opening times).</p>
                        <p style='margin:0 0 8px 0;'><strong>Your message:</strong></p>
                        <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;'>
                            {message}
                        </blockquote>
                        <p style='margin:0 0 12px 0;'><strong>What happens next?</strong></p>
                        <ol style='margin:0 0 16px 20px;padding:0;'>
                            <li>We confirm brand / model details if needed.</li>
                            <li>We provide an indicative call‑out / repair approach.</li>
                            <li>You choose a convenient visit window.</li>
                        </ol>
                        <p style='margin:0 0 16px 0;'>If anything is urgent you can call us directly on <strong>{current_app.config["BUSINESS_PHONE"]}</strong>.</p>
                        <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Business Hours: Mon–Fri 8:00–18:00 · Sat 9:00–16:00</p>
                        <p style='margin:0 0 24px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
                        <p style='margin:0;'>Kind regards,<br><strong>Osaco Appliance Repair Team</strong></p>
                        """

                        mail.send(business_msg)
                        mail.send(customer_msg)
                        return {'success': True}
                except Exception as e:
                        current_app.logger.error(f'Email sending error: {str(e)}')
                        return {'success': False, 'error': str(e)}

    # NEW UNIFIED METHOD
    def send_unified_service_email(self, data):
        """Generic service enquiry email builder to replace multiple specialised variants.

        Expected base fields: name, email, service, message (message optional if other detail fields present)
        Optional recognised detail fields (will be included automatically if present):
            phone, brand, model, issue, urgency, businessType,
            appliance, machineType, dishwasherType, washerType, equipmentType
        """
        try:
            # Normalise message
            base_message = data.get('message') or 'No additional details provided'

            # Collect dynamic detail rows excluding base identifiers
            ignore_keys = {'name', 'email', 'service', 'message'}
            detail_order = [
                'phone', 'brand', 'model', 'issue', 'urgency', 'businessType',
                'appliance', 'machineType', 'dishwasherType', 'washerType', 'equipmentType'
            ]
            details_html = ''
            for key in detail_order:
                if key in data and data[key]:
                    pretty_key = key.replace('Type', ' Type').replace('machine', 'Machine').replace('washer', 'Washer')
                    details_html += f"<p><strong>{pretty_key.capitalize()}:</strong> {data[key]}</p>"

            business_msg = Message(
                subject=f"Osaco Enquiry - {data.get('service', 'General')}",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )

            business_msg.html = f"""
            <h2 style='margin:0 0 12px 0;'>New Website Service Enquiry (Osaco)</h2>
            <p style='margin:0 0 4px 0;'><strong>Client:</strong> {data.get('name')} &lt;{data.get('email')}&gt;</p>
            <p style='margin:0 0 12px 0;'><strong>Requested Service:</strong> {data.get('service')}</p>
            {details_html if details_html else ''}
            <hr style='margin:16px 0;'>
            <p style='margin:0 0 4px 0;'><strong>Message / Details:</strong></p>
            <div style='background:#f5f7fa;padding:12px 16px;border-radius:4px;white-space:pre-line;'>{base_message}</div>
            <p style='margin:16px 0 0 0;font-size:12px;color:#555;'>Submitted {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """

            customer_msg = Message(
                subject=f"Osaco – {data.get('service')} enquiry received",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data.get('email')]
            )

            customer_msg.html = f"""
            <h2 style='margin:0 0 12px 0;'>We’ve got your request</h2>
            <p style='margin:0 0 12px 0;'>Hi {data.get('name')}, thanks for reaching out about <strong>{data.get('service')}</strong>.</p>
            <p style='margin:0 0 12px 0;'>An Osaco engineer will review the information you supplied and contact you shortly to arrange the next step.</p>
            {('<div style=\'margin:0 0 16px 0;\'><strong>Details Provided:</strong>' + details_html + '</div>') if details_html else ''}
            <p style='margin:0 0 4px 0;'><strong>Your message:</strong></p>
            <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;white-space:pre-line;'>{base_message}</blockquote>
            <p style='margin:0 0 12px 0;'><strong>Typical response window:</strong> within 1 business hour (Mon–Fri daytime).</p>
            <p style='margin:0 0 12px 0;'>Need something urgent? Call us on <strong>{current_app.config['BUSINESS_PHONE']}</strong>.</p>
            <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
            <p style='margin:0 0 0 0;'>Kind regards,<br><strong>Osaco Appliance Repair Team</strong></p>
            """

            mail.send(business_msg)
            mail.send(customer_msg)

            return {'success': True}
        except Exception as e:
            current_app.logger.error(f'Unified service email error: {str(e)}')
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
