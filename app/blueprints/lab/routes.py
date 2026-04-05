from flask import render_template
from app.blueprints.lab import bp

@bp.route("/")
def index():
    return render_template("lab/index.html")
