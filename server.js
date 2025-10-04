import express from 'express';
import cors from 'cors';
import nodemailer from 'nodemailer';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.set('trust proxy', 1); // Trust Railway's proxy for rate limiting
const PORT = process.env.PORT || 3001;

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: false
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});
app.use('/api/', limiter);

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Email configuration
const emailConfig = {
  host: process.env.MAIL_SERVER || 'smtp.gmail.com',
  port: parseInt(process.env.MAIL_PORT) || 587,
  secure: false, // true for 465, false for other ports
  auth: {
    user: process.env.MAIL_USERNAME,
    pass: process.env.MAIL_PASSWORD
  },
  tls: {
    rejectUnauthorized: false
  }
};

const transporter = nodemailer.createTransport(emailConfig);

// Test email configuration (don't fail if it doesn't work)
if (process.env.MAIL_USERNAME && process.env.MAIL_PASSWORD) {
  // Skip verification for now to allow server to start
  console.log('📧 Email service: Configured (verification skipped)');
} else {
  console.log('📧 Email service: Not configured (missing credentials)');
}

// Email service class
class EmailService {
  async sendContactEmail(name, email, phone, service, message) {
    try {
      console.log(`Sending contact email for ${service} from ${name} (${email})`);

      const businessMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: process.env.BUSINESS_EMAIL,
        subject: `O-TECH HOME SERVICES Website Contact - ${service}`,
        html: `
          <h2>New Website Enquiry (O-TECH HOME SERVICES)</h2>
          <p><strong>From:</strong> ${name} &lt;${email}&gt;</p>
          <p><strong>Phone:</strong> ${phone}</p>
          <p><strong>Service Selected:</strong> ${service}</p>
          <hr style='margin:16px 0;'>
          <p style='margin:0 0 4px 0;'><strong>Message:</strong></p>
          <p style='white-space:pre-line;margin-top:4px'>${message}</p>
          <hr style='margin:16px 0;'>
          <p style='font-size:12px;color:#555'>Submitted ${new Date().toISOString()}</p>
        `
      };

      const customerMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: email,
        subject: `O-TECH HOME SERVICES - We received your ${service} enquiry`,
        html: `
          <h2 style='margin:0 0 12px 0;'>Thank you - your enquiry is with our team</h2>
          <p style='margin:0 0 12px 0;'>Hi ${name},</p>
          <p style='margin:0 0 12px 0;'>We've received your request regarding <strong>${service}</strong>. An O-TECH HOME SERVICES technician will review the details and contact you (usually within 1 business hour during opening times).</p>
          <p style='margin:0 0 8px 0;'><strong>Your message:</strong></p>
          <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;'>
            ${message}
          </blockquote>
          <p style='margin:0 0 12px 0;'><strong>What happens next?</strong></p>
          <ol style='margin:0 0 16px 20px;padding:0;'>
            <li>We confirm brand / model details if needed.</li>
            <li>We provide an indicative call-out / repair approach.</li>
            <li>You choose a convenient visit window.</li>
          </ol>
          <p style='margin:0 0 16px 0;'>If anything is urgent you can call us directly on <strong>${process.env.BUSINESS_PHONE}</strong>.</p>
          <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Business Hours: Mon-Fri 8:00-18:00 - Sat 9:00-16:00</p>
          <p style='margin:0 0 24px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
          <p style='margin:0;'>Kind regards,<br>O-TECH HOME SERVICES Team</p>
        `
      };

      await transporter.sendMail(businessMailOptions);
      await transporter.sendMail(customerMailOptions);

      console.log(`Successfully sent contact emails for ${service}`);
      return { success: true };
    } catch (error) {
      console.error('Email sending error:', error);
      return { success: false, error: error.message };
    }
  }

  async sendUnifiedServiceEmail(data) {
    try {
      console.log(`Sending unified service email for ${data.service} from ${data.name} (${data.email})`);

      const baseMessage = data.message || 'No additional details provided';

      const detailOrder = [
        'phone', 'brand', 'model', 'issue', 'urgency', 'businessType',
        'appliance', 'machineType', 'dishwasherType', 'washerType', 'equipmentType'
      ];

      let detailsHtml = '';
      for (const key of detailOrder) {
        if (data[key]) {
          const prettyKey = key.replace('Type', ' Type').replace('machine', 'Machine').replace('washer', 'Washer');
          detailsHtml += `<p><strong>${prettyKey.charAt(0).toUpperCase() + prettyKey.slice(1)}:</strong> ${data[key]}</p>`;
        }
      }

      const businessMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: process.env.BUSINESS_EMAIL,
        subject: `O-TECH HOME SERVICES Enquiry - ${data.service}`,
        html: `
          <h2 style='margin:0 0 12px 0;'>New Website Service Enquiry (O-TECH HOME SERVICES)</h2>
          <p style='margin:0 0 4px 0;'><strong>Client:</strong> ${data.name} &lt;${data.email}&gt;</p>
          <p style='margin:0 0 12px 0;'><strong>Requested Service:</strong> ${data.service}</p>
          ${detailsHtml}
          <hr style='margin:16px 0;'>
          <p style='margin:0 0 4px 0;'><strong>Message / Details:</strong></p>
          <div style='background:#f5f7fa;padding:12px 16px;border-radius:4px;white-space:pre-line;'>${baseMessage}</div>
          <p style='margin:16px 0 0 0;font-size:12px;color:#555;'>Submitted ${new Date().toISOString()}</p>
        `
      };

      const customerMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: data.email,
        subject: `O-TECH HOME SERVICES - ${data.service} enquiry received`,
        html: `
          <h2 style='margin:0 0 12px 0;'>We've got your request</h2>
          <p style='margin:0 0 12px 0;'>Hi ${data.name}, thanks for reaching out about <strong>${data.service}</strong>.</p>
          <p style='margin:0 0 12px 0;'>An O-TECH HOME SERVICES engineer will review the information you supplied and contact you shortly to arrange the next step.</p>
          ${detailsHtml ? `<div style='margin:0 0 16px 0;'><strong>Details Provided:</strong>${detailsHtml}</div>` : ''}
          <p style='margin:0 0 4px 0;'><strong>Your message:</strong></p>
          <blockquote style='margin:0 0 16px 0;padding:12px 16px;background:#f5f7fa;border-left:4px solid #2563eb;border-radius:4px;white-space:pre-line;'>${baseMessage}</blockquote>
          <p style='margin:0 0 12px 0;'><strong>Typical response window:</strong> within 1 business hour (Mon-Fri daytime).</p>
          <p style='margin:0 0 12px 0;'>Need something urgent? Call us on <strong>${process.env.BUSINESS_PHONE}</strong>.</p>
          <p style='margin:0 0 4px 0;font-size:12px;color:#555'>Service Areas: Central, North, South, East, West & Greater London</p>
          <p style='margin:0 0 0 0;'>Kind regards,<br>O-TECH HOME SERVICES Team</p>
        `
      };

      await transporter.sendMail(businessMailOptions);
      await transporter.sendMail(customerMailOptions);

      console.log(`Successfully sent unified service emails for ${data.service}`);
      return { success: true };
    } catch (error) {
      console.error('Unified service email error:', error);
      return { success: false, error: error.message };
    }
  }

  async sendNewsletterSignup(email, name = '') {
    try {
      console.log(`Sending newsletter signup email to ${email}`);

      const welcomeMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: email,
        subject: `Welcome to ${process.env.BUSINESS_NAME} Newsletter!`,
        html: `
          <h2>Welcome to ${process.env.BUSINESS_NAME}!</h2>
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
          ${process.env.BUSINESS_NAME} Team</p>
        `
      };

      const businessMailOptions = {
        from: `"${process.env.BUSINESS_NAME}" <${process.env.MAIL_USERNAME}>`,
        to: process.env.BUSINESS_EMAIL,
        subject: 'New Newsletter Subscription',
        html: `
          <h2>New Newsletter Subscription</h2>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Name:</strong> ${name || 'Not provided'}</p>
          <p><strong>Subscribed:</strong> ${new Date().toISOString()}</p>
        `
      };

      await transporter.sendMail(welcomeMailOptions);
      await transporter.sendMail(businessMailOptions);

      console.log('Successfully sent newsletter signup emails');
      return { success: true };
    } catch (error) {
      console.error('Newsletter signup email error:', error);
      return { success: false, error: error.message };
    }
  }
}

const emailService = new EmailService();

// Routes
app.get('/api/health', (req, res) => {
  res.json({
    status: 'healthy',
    message: 'O-TECH HOME SERVICES API is running',
    version: '1.0.0',
    backend: 'Node.js/Express'
  });
});

app.get('/api/debug', (req, res) => {
  res.json({
    status: 'debug',
    environment: process.env.NODE_ENV || 'development',
    port: PORT,
    emailConfigured: !!(process.env.MAIL_USERNAME && process.env.MAIL_PASSWORD)
  });
});

app.get('/api/email-debug', (req, res) => {
  res.json({
    status: 'email_debug',
    config_status: {
      MAIL_SERVER: process.env.MAIL_SERVER,
      MAIL_PORT: process.env.MAIL_PORT,
      MAIL_USERNAME: !!(process.env.MAIL_USERNAME),
      MAIL_PASSWORD: !!(process.env.MAIL_PASSWORD),
      BUSINESS_EMAIL: process.env.BUSINESS_EMAIL,
      BUSINESS_NAME: process.env.BUSINESS_NAME,
      BUSINESS_PHONE: process.env.BUSINESS_PHONE
    },
    service_status: 'Email service initialized successfully',
    note: 'MAIL_USERNAME and MAIL_PASSWORD show as boolean for security'
  });
});

app.post('/api/contact', async (req, res) => {
  try {
    const { name, email, phone, service, message } = req.body;

    // Validation
    const requiredFields = ['name', 'email', 'phone', 'service', 'message'];
    const missingFields = requiredFields.filter(field => !req.body[field] || !req.body[field].trim());

    if (missingFields.length > 0) {
      return res.status(400).json({
        success: false,
        message: `Missing required fields: ${missingFields.join(', ')}`
      });
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid email format'
      });
    }

    const result = await emailService.sendContactEmail(name, email, phone, service, message);

    if (result.success) {
      res.json({
        success: true,
        message: 'Thank you for your inquiry! We will contact you soon.'
      });
    } else {
      res.status(500).json({
        success: false,
        message: 'Failed to send message. Please try again.'
      });
    }
  } catch (error) {
    console.error('Contact form error:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred. Please try again.'
    });
  }
});

app.post('/api/contact/enquiry', async (req, res) => {
  try {
    const data = req.body || {};

    const requiredFields = ['name', 'email', 'service'];
    const missingFields = requiredFields.filter(field => !data[field] || !data[field].trim());

    if (missingFields.length > 0) {
      return res.status(400).json({
        success: false,
        message: `Missing required fields: ${missingFields.join(', ')}`
      });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid email format'
      });
    }

    if (!(data.message || data.issue)) {
      return res.status(400).json({
        success: false,
        message: 'Please provide a message or issue description'
      });
    }

    const result = await emailService.sendUnifiedServiceEmail(data);

    if (result.success) {
      res.json({
        success: true,
        message: 'Thank you! We have received your enquiry.'
      });
    } else {
      res.status(500).json({
        success: false,
        message: 'Failed to send message. Please try again.'
      });
    }
  } catch (error) {
    console.error('Unified contact form error:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred. Please try again.'
    });
  }
});

// Legacy endpoints for compatibility
app.post('/api/contact/appliances', async (req, res) => {
  req.body.service = req.body.service || 'Appliance Repair';
  return app._router.handle(req, res, () => {});
});

app.post('/api/contact/coffee-machines', async (req, res) => {
  req.body.service = req.body.service || 'Coffee Machine Repair';
  return app._router.handle(req, res, () => {});
});

app.post('/api/contact/dishwashers', async (req, res) => {
  req.body.service = req.body.service || 'Dishwasher Repair';
  return app._router.handle(req, res, () => {});
});

app.post('/api/contact/washing-machines', async (req, res) => {
  req.body.service = req.body.service || 'Washing Machine Repair';
  return app._router.handle(req, res, () => {});
});

app.post('/api/contact/commercial-equipment', async (req, res) => {
  req.body.service = req.body.service || 'Commercial Equipment Repair';
  return app._router.handle(req, res, () => {});
});

app.post('/api/newsletter', async (req, res) => {
  try {
    const { email, name } = req.body;

    if (!email || !email.trim()) {
      return res.status(400).json({
        success: false,
        message: 'Email is required'
      });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid email format'
      });
    }

    const result = await emailService.sendNewsletterSignup(email, name);

    if (result.success) {
      res.json({
        success: true,
        message: 'Thank you for subscribing to our newsletter!'
      });
    } else {
      res.status(500).json({
        success: false,
        message: 'Failed to subscribe. Please try again.'
      });
    }
  } catch (error) {
    console.error('Newsletter signup error:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred. Please try again.'
    });
  }
});

// Serve static files from the dist directory (for production)
app.use(express.static('dist'));

// Catch all handler: send back index.html for client-side routing
app.get('*', (req, res) => {
  res.sendFile('index.html', { root: 'dist' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 O-TECH HOME SERVICES API running on port ${PORT}`);
  console.log(`📧 Email service: ${process.env.MAIL_USERNAME ? 'Configured' : 'Not configured'}`);
  console.log(`🌍 Environment: ${process.env.NODE_ENV || 'development'}`);
});

export default app;