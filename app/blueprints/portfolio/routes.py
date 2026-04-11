from flask import render_template
from app.blueprints.portfolio import bp

@bp.route("/")
def index():
    return render_template("portfolio/index.html")

@bp.route("/ee")
def ee():
    return render_template("portfolio/ee.html")

@bp.route("/ee/bldc-motor-control")
def bldc_motor_control():
    return render_template("portfolio/bldc_motor_control.html")

@bp.route("/ee/professional")
def professional():
    return render_template("portfolio/professional.html")

@bp.route("/se")
def se():
    return render_template("portfolio/se.html")

@bp.route("/me")
def me():
    return render_template("portfolio/me.html")
