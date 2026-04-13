# tedroflo.com — Personal Portfolio

Live at **[tedroflo.com](https://tedroflo.com)**

Personal portfolio site for Edwin Floyd — Electrical & Software Engineer. The site itself is a project: designed, built, and self-hosted from scratch on a single-board computer in a home lab.

## Stack

| Layer | Technology |
|---|---|
| Framework | Flask (Python) — blueprints, Jinja2 templates, SQLAlchemy ORM |
| Database | SQLite — resume and work history, queried live |
| CSS | Tailwind CSS v4 — standalone CLI, compiled via systemd watcher |
| WSGI | Gunicorn — serves Flask over a Unix socket |
| Reverse Proxy | Nginx — static files + proxy to Gunicorn |
| Tunnel | Cloudflare Tunnel — outbound-only, no open ports on the router |

## Hardware

- **Le Potato (Libre Computer AML-S905X-CC)** — ARM Cortex-A53 SBC running Debian 12 Bookworm. Hosts the Flask app, Gunicorn, and Nginx.
- **Raspberry Pi 3** — Runs `cloudflared` (Cloudflare Tunnel) and Pi-hole for network-level DNS filtering.

## Architecture

```
Browser → Cloudflare Edge → cloudflared (RPi3) → Nginx → Gunicorn → Flask → SQLite
```

No cloud compute. No managed hosting. No monthly bill.

## Structure

```
app/
├── blueprints/
│   ├── main/        # Home, About
│   ├── resume/      # Work history, skills
│   ├── portfolio/   # EE, SE, ME project pages
│   └── lab/         # Interactive visualizations (HTML5 Canvas)
├── models/          # SQLAlchemy models (Job, etc.)
├── static/          # CSS, images
└── templates/       # Jinja2 templates
```

## Running Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Tailwind CSS must be compiled separately. Download the [Tailwind standalone CLI](https://tailwindcss.com/blog/standalone-cli) and run:

```bash
./tailwindcss -i app/static/css/tailwind.css -o app/static/css/main.css --watch
```
