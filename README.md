Minions_site Capstone
## How I completed the task (process & decisions)

Please mark this repo and commit:
- Canonical repo: https://github.com/MrsWinchester/minions1  
- Commit: <cff3f10305f8108ebd1efb273ae73a1f471ea5a9>

py -m venv .venv && ..venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver

Visit http://127.0.0.1:8000/

**Project entry points in _minions1_:**
- `manage.py` (repo root)
- `band/`, `minions_site/`
- Docs HTML: `docs/build/html/index.html` (see also `modules.html`)
- `Dockerfile`, `requirements.txt`

Quick run:

**Goal:** Build a small Django site (`minions_site`) with a `band` app, document it with Sphinx, and provide Docker support.

## Prerequisites
Python 3.12+, pip, Git
(Optional) Docker Desktop
Windows PowerShell commands shown below (macOS/Linux: replace py with python3 and paths accordingly)

### Steps I followed
1. **Django project & app**
   - Created project `minions_site` and app `band`.
   - Added models: `BandMember` (name, role) and `Show` (date, title, venue, city, price, is_sold_out).
   - Views: `home`, `about`, `ShowList` (paginated), and a simple `SignUp` view using Django auth forms.
   - Templates for home/about/shows/registration with basic styling and “Sold out” badges.

2. **Configuration & .env**
   - Loaded secrets via `python-dotenv` in `minions_site/settings.py`.
   - `.env` example:
     ```ini
     SECRET_KEY=replace_me
     DEBUG=True
     ALLOWED_HOSTS=*
     ```
3) Run locally (quick start)
From the project root (the folder containing manage.py and Dockerfile):
# create & activate venv
py -m venv .venv
.\.venv\Scripts\Activate
# install deps
pip install -r requirements.txt
# migrate & run
py manage.py migrate
py manage.py runserver

Open http://127.0.0.1:8000 (or http://localhost:8000
— The home page lists upcoming shows.

4) **Sphinx documentation**
   - Enabled `autodoc` and used `sphinx-apidoc` to generate RST stubs for `band` and `minions_site`.
   - Built HTML with:
     ```powershell
     .\docs\make.bat html
     ```
   - Committed the generated HTML so reviewers can open:
     - `docs/build/html/index.html`
     - `docs/build/html/modules.html` → shows `band.models` and `band.views`.

5) Docker (dev)
From the project root (where manage.py and Dockerfile live):
docker build -t minions_site:dev .
docker run --rm -p 8000:8000 --env-file .\.env minions_site:dev
Then browse http://localhost:8000

6) Repository layout
minions_site/
├─ manage.py
├─ Dockerfile
├─ band/                  # app (models, views, urls, templates/…)
├─ docs/
│  ├─ source/             # Sphinx sources (conf.py, *.rst)
│  └─ build/html/         # Generated HTML (index.html, modules.html)
├─ README.md
└─ requirements.txt

7) Notes / verification
Links in this README are angle-bracketed so they’re clickable on GitHub.
Docs build verified; modules page lists the app modules.
Docker run binds 0.0.0.0:8000 → host :8000.



