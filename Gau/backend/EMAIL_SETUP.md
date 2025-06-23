# 📧 Email Configuration Guide

## Current Status
✅ **Test script removed**  
✅ **Email routes configured**  
✅ **Email service implemented**  
🔧 **Email credentials needed for production**

## Email Routes Available

### 📋 General Contact
- **Endpoint**: `POST /api/contact`
- **Fields**: name, email, service, message

### 🔧 Service-Specific Contact Forms
- **Appliances**: `POST /api/contact/appliances`
- **Coffee Machines**: `POST /api/contact/coffee-machines`
- **Dishwashers**: `POST /api/contact/dishwashers` 
- **Washing Machines**: `POST /api/contact/washing-machines`
- **Commercial Equipment**: `POST /api/contact/commercial-equipment`

### 📨 Newsletter
- **Endpoint**: `POST /api/newsletter`
- **Fields**: email, name (optional)

## Email Configuration

### 🔑 Production Setup
To enable real email functionality, update these values in `.env`:

```env
# Email server settings
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-business-email@gmail.com
MAIL_PASSWORD=your-app-specific-password

# Business contact info
BUSINESS_EMAIL=your-business-email@gmail.com
BUSINESS_NAME=Your Business Name
BUSINESS_PHONE=Your Phone Number
```

### 📧 Gmail Setup (Recommended)
1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App Passwords
   - Generate password for "Mail" 
3. **Use App Password** in `MAIL_PASSWORD` (not your regular password)

### 🔒 Proton Mail Setup
1. **Enable Bridge or use App Password**:
   - **Option A - Proton Mail Bridge** (Recommended):
     - Download and install Proton Mail Bridge
     - Use Bridge's generated credentials
     - SMTP: 127.0.0.1:1025 (local Bridge)
   
   - **Option B - Direct SMTP** (Current setup):
     - Use Proton Mail's SMTP server directly
     - **Important**: You need a **Proton Mail Plus** subscription for SMTP access
     - Generate an app-specific password in Proton Mail settings

2. **Proton Mail SMTP Settings**:
```env
MAIL_SERVER=smtp.protonmail.ch
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@proton.me
MAIL_PASSWORD=your-app-password
```

⚠️ **Important for Proton Mail**:
- Free Proton accounts don't have SMTP access
- You need **Proton Mail Plus** ($4/month) or higher plan
- Create an app-specific password in Settings → Security

### 🏢 Other Email Providers
Update these settings for different providers:

**Outlook/Hotmail:**
```env
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

**Yahoo:**
```env
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

**Custom SMTP:**
```env
MAIL_SERVER=your-smtp-server.com
MAIL_PORT=587 # or 465 for SSL
MAIL_USE_TLS=True # or False for SSL
```

## Features Implemented

### ✅ Automatic Email Functions
- **Business Notifications**: All form submissions are sent to business email
- **Customer Confirmations**: Automatic confirmation emails to customers
- **Input Validation**: Email format and required field validation
- **Error Handling**: Graceful error handling and logging
- **Service-Specific Templates**: Different email templates for each service

### ✅ Email Templates Include
- Customer name and contact information
- Service type and specific details
- Issue description and urgency
- Professional branded templates
- Timestamp of submission

## Testing Email Functionality

### 🧪 Development Testing
Currently emails will not send because placeholder credentials are used. To test:

1. **Update credentials** in `.env` with real email settings
2. **Restart Flask server**
3. **Submit test form** through frontend
4. **Check email inbox** for notifications

### 🔍 Debugging
Check Flask server logs for email errors:
- Email sending attempts are logged
- Error messages show specific email failures
- Validation errors are clearly reported

## Next Steps

1. **Configure Real Email Credentials** for production use
2. **Test Email Functionality** with real email settings
3. **Customize Email Templates** with your branding
4. **Set Up Email Monitoring** for production environment

---

**Current Backend Status**: ✅ Ready for email integration  
**Frontend Integration**: ✅ Contact forms ready to connect  
**Production Ready**: 🔧 Needs email credentials
