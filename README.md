# minions1

Django project: **minions_site** package with `band` app.

## Setup (Windows, venv)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
