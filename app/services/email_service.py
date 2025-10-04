from flask import current_app
from flask_mail import Message
from app import mail
from datetime import datetime
import threading

class EmailService:
    def _send_email_async(self, msg):
        """Send email asynchronously in a background thread"""
        try:
            mail.send(msg)
        except Exception as e:
            current_app.logger.error(f'Async email sending error: {str(e)}')

    def send_contact_email(self, name, email, phone, service, message):
        try:
            business_msg = Message(
                subject=f'O-TECH HOME SERVICES Website Contact - {service}',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )

            business_msg.html = f"""
            <h2>New Website Enquiry (O-TECH HOME SERVICES)</h2>
            <p><strong>From:</strong> {name} &lt;{email}&gt;</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Service Selected:</strong> {service}</p>
            <hr style='margin:16px 0;'>
            <p style='margin:0 0 4px 0;'><strong>Message:</strong></p>
            <p style='white-space:pre-line;margin-top:4px'>{message}</p>
            <hr style='margin:16px 0;'>
            <p style='font-size:12px;color:#555'>Submitted {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (server time)</p>
            """

            customer_msg = Message(
                subject=f'O-TECH HOME SERVICES - We received your {service} enquiry',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[email]
            )

            customer_msg.html = f"""
            <h2 style='margin:0 0 12px 0;'>Thank you - your enquiry is with our team</h2>
            <p style='margin:0 0 12px 0;'>Hi {name},</p>
            <p style='margin:0 0 12px 0;'>We've received your request regarding <strong>{service}</strong>. An O-TECH HOME SERVICES technician will review the details and contact you (usually within 1 business hour during opening times).</p>
            <p style='margin:0 0 8px 0;'><strong>Your message:</strong></p>
            <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;'>
              {message}
            </blockquote>
            <p style='margin:0 0 12px 0;'><strong>What happens next?</strong></p>
            <ol style='margin:0 0 16px 20px;padding:0;'>
              <li>We confirm brand / model details if needed.</li>
              <li>We provide an indicative call-out / repair approach.</li>
              <li>You choose a convenient visit window.</li>
            </ol>
            <p style='margin:0 0 16px 0;'>If anything is urgent you can call us directly on <strong>{current_app.config["BUSINESS_PHONE"]}</strong>.</p>
            <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Business Hours: Mon-Fri 8:00-18:00 - Sat 9:00-16:00</p>
            <p style='margin:0 0 24px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
            <p style='margin:0;'>Kind regards,<br>O-TECH HOME SERVICES Team</p>
            """

            # Send emails asynchronously
            threading.Thread(target=self._send_email_async, args=(business_msg,)).start()
            threading.Thread(target=self._send_email_async, args=(customer_msg,)).start()
            
            return {'success': True}
        except Exception as e:
            current_app.logger.error(f'Email sending error: {str(e)}')
            return {'success': False, 'error': str(e)}

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
                subject=f"O-TECH HOME SERVICES Enquiry - {data.get('service', 'General')}",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['BUSINESS_EMAIL']]
            )

            business_msg.html = f"""
            <h2 style='margin:0 0 12px 0;'>New Website Service Enquiry (O-TECH HOME SERVICES)</h2>
            <p style='margin:0 0 4px 0;'><strong>Client:</strong> {data.get('name')} &lt;{data.get('email')}&gt;</p>
            <p style='margin:0 0 12px 0;'><strong>Requested Service:</strong> {data.get('service')}</p>
            {details_html if details_html else ''}
            <hr style='margin:16px 0;'>
            <p style='margin:0 0 4px 0;'><strong>Message / Details:</strong></p>
            <div style='background:#f5f7fa;padding:12px 16px;border-radius:4px;white-space:pre-line;'>{base_message}</div>
            <p style='margin:16px 0 0 0;font-size:12px;color:#555;'>Submitted {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            """

            customer_msg = Message(
                subject=f"O-TECH HOME SERVICES - {data.get('service')} enquiry received",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[data.get('email')]
            )

            # Build details HTML for customer email with proper escaping
            details_display = ''
            if details_html:
                details_display = f"<div style='margin:0 0 16px 0;'><strong>Details Provided:</strong>{details_html}</div>"

            customer_msg.html = f"""
            <h2 style='margin:0 0 12px 0;'>We've got your request</h2>
            <p style='margin:0 0 12px 0;'>Hi {data.get('name')}, thanks for reaching out about <strong>{data.get('service')}</strong>.</p>
            <p style='margin:0 0 12px 0;'>An O-TECH HOME SERVICES engineer will review the information you supplied and contact you shortly to arrange the next step.</p>
            {details_display}
            <p style='margin:0 0 4px 0;'><strong>Your message:</strong></p>
            <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;white-space:pre-line;'>{base_message}</blockquote>
            <p style='margin:0 0 12px 0;'><strong>Typical response window:</strong> within 1 business hour (Mon-Fri daytime).</p>
            <p style='margin:0 0 12px 0;'>Need something urgent? Call us on <strong>{current_app.config['BUSINESS_PHONE']}</strong>.</p>
            <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
            <p style='margin:0 0 0 0;'>Kind regards,<br>O-TECH HOME SERVICES Team</p>
            """

            # Send emails asynchronously
            threading.Thread(target=self._send_email_async, args=(business_msg,)).start()
            threading.Thread(target=self._send_email_async, args=(customer_msg,)).start()

            return {'success': True}
        except Exception as e:
            current_app.logger.error(f'Unified service email error: {str(e)}')
            return {'success': False, 'error': str(e)}

    def _prepare_specialised_payload(self, data, default_service):
        payload = dict(data)
        payload['service'] = data.get('service') or default_service

        if not payload.get('message'):
            message_parts = []
            if data.get('issue'):
                message_parts.append(f"Issue: {data['issue']}")
            if data.get('urgency'):
                message_parts.append(f"Urgency: {data['urgency']}")
            if data.get('model'):
                message_parts.append(f"Model: {data['model']}")
            payload['message'] = '\n'.join(message_parts) if message_parts else 'No additional details provided'

        return payload

    def send_appliance_service_email(self, data):
        payload = self._prepare_specialised_payload(data, 'Appliance Repair')
        return self.send_unified_service_email(payload)

    def send_coffee_machine_service_email(self, data):
        payload = self._prepare_specialised_payload(data, 'Coffee Machine Service')
        payload.setdefault('machineType', data.get('machineType'))
        return self.send_unified_service_email(payload)

    def send_dishwasher_service_email(self, data):
        payload = self._prepare_specialised_payload(data, 'Dishwasher Repair')
        payload.setdefault('dishwasherType', data.get('dishwasherType'))
        return self.send_unified_service_email(payload)

    def send_washing_machine_service_email(self, data):
        payload = self._prepare_specialised_payload(data, 'Washing Machine Repair')
        payload.setdefault('washerType', data.get('washerType'))
        return self.send_unified_service_email(payload)

    def send_commercial_equipment_service_email(self, data):
        payload = self._prepare_specialised_payload(data, 'Commercial Equipment Repair')
        payload.setdefault('equipmentType', data.get('equipmentType'))
        payload.setdefault('businessType', data.get('businessType'))
        return self.send_unified_service_email(payload)

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
            
            # Send emails asynchronously
            threading.Thread(target=self._send_email_async, args=(welcome_msg,)).start()
            threading.Thread(target=self._send_email_async, args=(business_msg,)).start()
            
            return {'success': True}
            
        except Exception as e:
            current_app.logger.error(f'Newsletter signup email error: {str(e)}')
            return {'success': False, 'error': str(e)}
