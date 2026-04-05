from flask import render_template
from app.blueprints.portfolio import bp

@bp.route("/")
def index():
    return render_template("portfolio/index.html")

@bp.route("/ee")
def ee():
    return render_template("portfolio/ee.html")

@bp.route("/se")
def se():
    return render_template("portfolio/se.html")
