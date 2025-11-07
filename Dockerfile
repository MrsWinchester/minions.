# Dockerfile (dev)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Use your Django settings module
ENV DJANGO_SETTINGS_MODULE=minions_site.settings

# Expose dev server port
EXPOSE 8000

# Run migrations then start the dev server (simple for demo/dev)
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
