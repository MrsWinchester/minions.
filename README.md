Minions_site Capstone

Please mark this repo and commit:
- Canonical repo: https://github.com/MrsWinchester/minions1  
- Commit: eca7945
- Permalink: <https://github.com/MrsWinchester/minions1/tree/eca7945>

**Goal:**
Build a small Django site (minions_site) with a band app, document it with Sphinx, and provide Docker support.

## Prerequisites
Python 3.12+, pip, Git
(Optional) Docker Desktop
Shell used here: Windows PowerShell (on macOS/Linux, use python3 and source .venv/bin/activate)

1) Setup & run locally (quick start)
From the repo root (where manage.py and Dockerfile live):
# create & activate a virtual environment
py -m venv .venv
.\.venv\Scripts\Activate

# install dependencies
pip install -r requirements.txt

Create your .env file
Create a file named .env in the repo root:

SECRET_KEY=replace_me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

The project loads this file via python-dotenv in minions_site/settings.py.

Migrate & start the dev server
py manage.py migrate
py manage.py runserver

Open to see homepage with upcoming shows: 
http://127.0.0.1:8000
 or http://localhost:8000
 
2) Build & view Sphinx documentation
Autodoc is enabled and stubs were generated for band and minions_site.
'''powershell:
.\docs\make.bat html
Open:
docs/build/html/index.html
docs/build/html/modules.html (shows band.models and band.views)

If the index page is not linked to the modules, to ensure docs/source/index.rst it has:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Build: .\docs\make.bat clean and .\docs\make.bat html.

3) Run with Docker (dev):
'''Powershell:
docker build -t minions_site:dev .
docker run --rm -p 8000:8000 --env-file .\.env minions_site:dev

Browse http://localhost:8000

The container runs migrations before the server starts (see Dockerfile’s CMD).

4) Repository layout (root)
minions1/
├─ manage.py
├─ band/                 # the app
├─ minions_site/         # the project package (only one copy)
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ docs/
│  ├─ source/            # Sphinx sources (conf.py, *.rst)
│  └─ build/html/        # Generated HTML (index.html, modules.html)
├─ Dockerfile
├─ requirements.txt
└─ README.md

5) Troubleshooting:
ERR_CONNECTION_REFUSED: the server needs to be running (py manage.py runserver) and visiting the correct port (8000).

ALLOWED_HOSTS error: Ensure the .env exists and includes:
ALLOWED_HOSTS=127.0.0.1,localhost.

Port already in use:
'''powershell:
netstat -ano | findstr :8000
taskkill /PID <PID_FROM_OUTPUT> /F

Then rerun the server.

Notes / verification:
Links are angle-bracketed so they’re clickable on GitHub.
Docs build verified; modules.html lists band.models & band.views.
Docker maps container 0.0.0.0:8000 to host :8000.




