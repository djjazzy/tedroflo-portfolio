from flask import render_template
from app.blueprints.resume import bp

@bp.route("/")
def index():
    return render_template("resume/index.html")
