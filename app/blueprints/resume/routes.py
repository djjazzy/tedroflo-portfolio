from flask import render_template
from app.blueprints.resume import bp
from app.models import Job

skills = {
    "Electrical Engineering": [
        "PCB Design (Altium, Cadence/OrCAD, Fusion 360)",
        "Power Electronics",
        "Sensor Integration (pressure, temperature, proximity, RFID, flow)",
        "Motor Control (PID, solenoids, servos)",
        "Signal Processing",
        "RF / Wireless",
        "LTspice",
    ],
    "Software Engineering": [
        "Python / Flask",
        "C / C++ / Qt / QML",
        "Embedded Firmware (ESP32, ARM, MIPS)",
        "Linux / Debian / BSP / sysfs",
        "LabVIEW / MATLAB / Octave",
        "Git / TDD / Scrum / OOP Design Patterns",
    ],
    "Tools & Platforms": [
        "Raspberry Pi / Le Potato / NXP iMX6",
        "Autodesk Fusion 360 / SolidWorks",
        "National Instruments cDAQ / DMM / Oscilloscopes",
        "MQTT / I2C / CAN / UART / GPIB",
        "Nginx / Gunicorn / Cloudflare",
        "3D Printing (Dremel 45)",
    ],
}

@bp.route("/")
def index():
    jobs = Job.query.order_by(Job.start_date.desc()).all()
    return render_template(
        "resume/index.html",
        jobs=jobs,
        skills=skills
    )
