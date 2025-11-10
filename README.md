# Capstone Project: Minions1

**Canonical repo:** https://github.com/MrsWinchester/minions1
**Commit:** 558d30c
**Permalink:** https://github.com/MrsWinchester/minions1/tree/558d30c

Django project: **minions_site** (project) with **band** (app).  
Includes Sphinx docs, optional Docker image, and a tiny seed snippet.

---

## Quickstart (Windows, PowerShell)

```powershell
# Clone and enter
git clone https://github.com/MrsWinchester/minions1
cd minions1

# Create & activate venv
py -m venv .venv
.\.venv\Scripts\Activate

# Install deps
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

Create a .env
The project loads this via python-dotenv in minions_site/settings.py.
SECRET_KEY=replace_me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

Migrate, create admin, run
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver

Open: http://127.0.0.1:8000/

(Optional) Seed some data quickly
py manage.py shell

from datetime import date
from band.models import BandMember, Show

BandMember.objects.get_or_create(name="Minnie",  role="Vocals")
BandMember.objects.get_or_create(name="Kevin",   role="Guitar")
BandMember.objects.get_or_create(name="Natasha", role="Drums")

Show.objects.get_or_create(
    title="KZN Live",
    venue="Town Hall",
    city="Durban",
    date=date(2025, 11, 20),
    price=0,
    is_sold_out=False,
)
exit()

Or add items in /admin:
• Band members → show on the About page
• Shows → show on the Shows page

2) Sphinx Documentation

Built HTML is committed under docs/build/html for reviewers.
Rebuild locally (optional):
# Clean & rebuild to docs/build/html
.\docs\make.bat clean
.\docs\make.bat html

# Or with pure Python:
py -m sphinx -b html docs/source docs/build/html

# Open the landing page
start docs\build\html\index.html

3) Run with Docker (optional)
# Build the image
docker build -t minions1 .

# Run (use your .env for SECRET_KEY/ALLOWED_HOSTS)
docker run --rm -p 8000:8000 --env-file .\.env minions1
# Browse: http://localhost:8000/

4) Project Structure (key bits)
minions1/
├─ manage.py
├─ band/                # app: models, views, templates
├─ minions_site/        # project: settings, urls, asgi/wsgi
├─ docs/
│  ├─ source/           # Sphinx sources (conf.py, *.rst)
│  └─ build/
│     └─ html/          # Built documentation (index.html, modules.html, ...)
├─ Dockerfile
├─ requirements.txt
├─ .env                 # not committed (example above)
└─ README.md

5) Troubleshooting

ALLOWED_HOSTS error: ensure .env has
ALLOWED_HOSTS=127.0.0.1,localhost and DEBUG=True for local dev.

Docs complain about dotenv:
py -m pip install python-dotenv sphinx-autodoc-typehints

py not found on your system: use python instead of py.

---



