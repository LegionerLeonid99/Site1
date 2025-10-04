// Quick email test script
import dotenv from 'dotenv';
import sgMail from '@sendgrid/mail';

dotenv.config();

// Initialize SendGrid
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

console.log('🧪 Testing SendGrid Email...\n');

const testEmail = {
  to: process.env.BUSINESS_EMAIL, // Send to yourself
  from: process.env.BUSINESS_EMAIL, // Must be verified in SendGrid
  subject: '🧪 Test Email from O-TECH HOME SERVICES',
  html: `
    <h2>Test Email Successful! ✅</h2>
    <p>If you're reading this, your SendGrid integration is working perfectly!</p>
    <p><strong>Tested at:</strong> ${new Date().toISOString()}</p>
    <hr>
    <p style="color: #666; font-size: 12px;">
      This is a test email from your local development environment.
    </p>
  `
};

try {
  console.log(`📧 Sending test email to: ${process.env.BUSINESS_EMAIL}`);
  await sgMail.send(testEmail);
  console.log('✅ SUCCESS! Email sent successfully!');
  console.log(`📬 Check your inbox: ${process.env.BUSINESS_EMAIL}\n`);
} catch (error) {
  console.error('❌ ERROR sending email:', error.message);
  if (error.response) {
    console.error('Response body:', error.response.body);
  }
  process.exit(1);
}
