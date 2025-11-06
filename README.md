## How I completed the task (process & decisions)

**Goal:** Build a small Django site (`minions_site`) with a `band` app, document it with Sphinx, and provide Docker support.

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

3. **Sphinx documentation**
   - Enabled `autodoc` and used `sphinx-apidoc` to generate RST stubs for `band` and `minions_site`.
   - Built HTML with:
     ```powershell
     .\docs\make.bat html
     ```
   - Committed the generated HTML so reviewers can open:
     - `docs/build/html/index.html`
     - `docs/build/html/modules.html` → shows `band.models` and `band.views`.

4. **Docker**
   - Added a dev `Dockerfile` that installs `requirements.txt`, runs migrations, and serves on `0.0.0.0:8000`.
   - Commands:
     ```powershell
     docker build -t minions_site:dev .
     docker run --rm -p 8000:8000 --env-file .\.env minions_site:dev
     ```

5. **Verification**
   - Local run:
     ```powershell
     py manage.py migrate
     py manage.py runserver
     ```
     Visit http://127.0.0.1:8000 – home page lists upcoming shows.
   - Docs: open `docs/build/html/index.html` (and `modules.html`).
   - Docker run: visit http://localhost:8000.

### Repository layout
