from flask import render_template
from app.blueprints.portfolio import bp

@bp.route("/")
def index():
    return render_template("portfolio/index.html")

@bp.route("/illustrations")
def illustrations():
    return render_template("portfolio/illustrations.html")

@bp.route("/illustrations/bldc-motor-control")
def bldc_motor_control():
    return render_template("portfolio/bldc_motor_control.html")

@bp.route("/professional")
def professional():
    return render_template("portfolio/professional.html")
