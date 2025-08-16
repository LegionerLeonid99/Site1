from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from config.config import config
import os

mail = Mail()

def create_app(config_name='default'):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  # Initialize extensions
  mail.init_app(app)

  # Configure CORS
  allow_null = os.getenv('ALLOW_NULL_ORIGIN', 'false').lower() == 'true'
  debug_mode = app.config.get('DEBUG', False)
  # In development allow all origins unless explicitly disabled
  if debug_mode and os.getenv('DISABLE_DEV_WILDCARD_CORS', 'false').lower() != 'true':
    CORS(app, resources={r"/api/*": {"origins": "*"}}, allow_headers=["Content-Type"], supports_credentials=False)
  else:
    origins = app.config.get('ALLOWED_ORIGINS', [])
    if allow_null:
      origins.append('null')
    CORS(app, resources={r"/api/*": {"origins": origins}}, allow_headers=["Content-Type"], supports_credentials=True)

  # Register blueprints
  from app.routes.contact import contact_bp
  from app.routes.newsletter import newsletter_bp
  from app.routes.health import health_bp

  app.register_blueprint(contact_bp, url_prefix='/api')
  app.register_blueprint(newsletter_bp, url_prefix='/api')
  app.register_blueprint(health_bp, url_prefix='/api')

  return app
