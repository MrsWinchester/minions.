Minions_site Capstone

Please mark this repo and commit:
- Canonical repo: https://github.com/MrsWinchester/minions1  
- Commit: eca7945
- Permalink: <https://github.com/MrsWinchester/minions1/tree/eca7945>

## How I completed the task (process & decisions)

**Goal:** Build a small Django site (`minions_site`) with a `band` app, document it with Sphinx, and provide Docker support.

## Prerequisites
Python 3.12+, pip, Git
(Optional) Docker Desktop
Shell: **Windows PowerShell** (macOS/Linux: use `python3` and `source .venv/bin/activate`)

## Run locally (quick start)

From the project root (the folder with `manage.py` and `Dockerfile`):

powershell
# create & activate venv
py -m venv .venv
.\.venv\Scripts\Activate

# install deps
pip install -r requirements.txt

# migrate & run
py manage.py migrate
py manage.py runserver

Open http://127.0.0.1:8000 (or http://localhost:8000) to see the homepage with upcoming shows

## Sphinx documentation
Autodoc is enabled; RST stubs were generated for band and minions_site.
Build HTML:
.\docs\make.bat html

Open:
docs/build/html/index.html
docs/build/html/modules.html (shows band.models and band.views)

## Docker (dev)
From the project root:
docker build -t minions_site:dev .
docker run --rm -p 8000:8000 --env-file .\.env minions_site:dev

Then browse http://localhost:8000

Steps I followed (summary)
1. Django project & app
Project minions_site, app band.
Models: BandMember (name, role), Show (date, title, venue, city, price, is_sold_out).
Views: home, about, ShowList (paginated), SignUp (Django auth).
Templates for home/about/shows/registration; “Sold out” badge styling.

2. Configuration & .env
Secrets loaded via python-dotenv in minions_site/settings.py.
Example .env:
SECRET_KEY=replace_me
DEBUG=True
ALLOWED_HOSTS=*

3. Docs
sphinx-apidoc used; HTML built and committed for easy review.

4. Repository layout
minions_site/
├─ manage.py
├─ Dockerfile
├─ band/                  # app (models, views, urls, templates/…)
├─ docs/
│  ├─ source/             # Sphinx sources (conf.py, *.rst)
│  └─ build/html/         # Generated HTML (index.html, modules.html)
├─ README.md
└─ requirements.txt

5. Notes / verification
Links are angle-bracketed for clickability on GitHub.
Docs build verified; Modules page lists band.models & band.views.
Docker runs on 0.0.0.0:8000 in the container, mapped to host :8000.

