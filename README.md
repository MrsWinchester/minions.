# Capstone Project: Minions1

Django project: **minions_site** package with **band** app.  
Includes Sphinx docs, optional Docker image, and a minimal seed script.

---

## Quickstart (Windows, PowerShell)

'''powershell
# Clone and enter
git clone https://github.com/MrsWinchester/minions1
cd minions1

# Create & activate venv
py -m venv .venv
.\.venv\Scripts\Activate

# Install deps
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

# Migrate DB and create a superuser
py manage.py migrate
py manage.py createsuperuser

# Run the server
py manage.py runserver

Open: http://127.0.0.1:8000/

# 3 quick things in Django Admin (to make pages show real data)
Go to /admin and sign in.
Band members: add a few members (name + role + optional bio).
These appear on the About page.
Shows: add one or two Show entries (title, venue, city, date, price, sold_out).
These appear on the Shows page.

Tip: If you prefer a one-shot seed, run:
'''Powershell
py manage.py shell

then paste:

from band.models import BandMember, Show
BandMember.objects.get_or_create(name="Minnie", role="Vocals")
BandMember.objects.get_or_create(name="Kevin", role="Guitar")
BandMember.objects.get_or_create(name="Natasha", role="Drums")
Show.objects.get_or_create(title="KZN Live", venue="Town Hall", city="Durban")
exit()

# Build the Sphinx Documentation
The project already commits built HTML in docs/build/html.
If you want to rebuild locally:
# Rebuild HTML to docs/build/html
py -m sphinx -b html docs/source docs/build/html

# Open the landing page locally
start docs\build\html\index.html

# Run with Docker (optional)
'''powershell
# Build
docker build -t minions1 .

# Run (port 8000)
docker run -p 8000:8000 minions1

Visit: http://localhost:8000/

If you need to run migrations inside the container:

'''powershell
docker run -it --rm -p 8000:8000 minions1 bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Project Structure (key bits)
band/                # app: models, views, templates
minions_site/        # project: settings, urls, asgi/wsgi
docs/                # Sphinx docs (source + build/html)
Dockerfile
manage.py
requirements.txt

# Troubleshooting
If docs complain about dotenv, just install it:
'''powershell
py -m pip install python-dotenv

If py isn’t recognized, try python instead.

---

