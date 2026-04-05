from flask import Blueprint
bp = Blueprint("resume", __name__, template_folder="templates")
from app.blueprints.resume import routes
