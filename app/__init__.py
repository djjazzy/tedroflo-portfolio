from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.blueprints.main import bp as main_bp
    from app.blueprints.resume import bp as resume_bp
    from app.blueprints.portfolio import bp as portfolio_bp
    from app.blueprints.lab import bp as lab_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(resume_bp, url_prefix="/resume")
    app.register_blueprint(portfolio_bp, url_prefix="/portfolio")
    app.register_blueprint(lab_bp, url_prefix="/lab")

    return app
