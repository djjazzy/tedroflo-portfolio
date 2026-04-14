import csv
import sys
from datetime import datetime
from wsgi import app
from app.models import db, Job

def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None

def import_jobs(csv_path):
    with app.app_context():
        db.create_all()

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0

            for row in reader:
                company = row["company"].strip()
                title   = row["job_title"].strip()
                start   = parse_date(row["job_start"])
                end     = parse_date(row["job_end"])
                desc    = row["job_description"].strip()

                existing = Job.query.filter_by(
                    title=title,
                    start_date=start
                ).first()

                if existing:
                    print(f"  Skipping (already exists): {title} at {company}")
                    continue

                job = Job(
                    company     = company,
                    title       = title,
                    start_date  = start,
                    end_date    = end,
                    description = desc,
                    is_current  = (end is None),
                )
                db.session.add(job)
                count += 1
                print(f"  Imported: {title} at {company}")

            db.session.commit()
            print(f"\nDone — {count} jobs imported.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "eflo_joblisting.csv"
    import_jobs(path)
