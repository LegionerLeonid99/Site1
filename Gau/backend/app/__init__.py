from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from config.config import config

mail = Mail()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    mail.init_app(app)
      # Configure CORS - Allow all origins during development
    CORS(app, origins="*", supports_credentials=True)
    
    # Register blueprints
    from app.routes.contact import contact_bp
    from app.routes.newsletter import newsletter_bp
    from app.routes.health import health_bp
    
    app.register_blueprint(contact_bp, url_prefix='/api')
    app.register_blueprint(newsletter_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix='/api')
    
    return app
