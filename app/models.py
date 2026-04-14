from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = "jobs"

    id          = db.Column(db.Integer, primary_key=True)
    company     = db.Column(db.String(100), nullable=False)
    title       = db.Column(db.String(100), nullable=False)
    start_date  = db.Column(db.Date, nullable=False)
    end_date    = db.Column(db.Date, nullable=True)
    description = db.Column(db.Text, nullable=False)
    is_current  = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Job {self.title} at {self.company}>"

    @property
    def start_formatted(self):
        return self.start_date.strftime("%b %Y")

    @property
    def end_formatted(self):
        return "Present" if self.is_current else self.end_date.strftime("%b %Y")
