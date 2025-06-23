import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Email settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Business settings
    BUSINESS_EMAIL = os.environ.get('BUSINESS_EMAIL') or 'info@fixitappliances.com'
    BUSINESS_NAME = os.environ.get('BUSINESS_NAME') or 'FixIt Appliances'
    BUSINESS_PHONE = os.environ.get('BUSINESS_PHONE') or '(555) 123-4567'
    
    # Frontend URL for CORS
    FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://localhost:5173'
    
    # API settings
    API_RATE_LIMIT = int(os.environ.get('API_RATE_LIMIT') or 100)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
