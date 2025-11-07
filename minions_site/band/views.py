# band/views.py
from __future__ import annotations

from typing import Any

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from .models import BandMember, Show

"""Views for the `band` app.

- `home`: shows the next three upcoming shows on the homepage.
- `about`: lists all band members alphabetically.
- `ShowList`: list view of shows (ordered by date).
- `SignUp`: simple user registration using Django’s `UserCreationForm`.
"""


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with the next three upcoming shows.

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Renders `band/home.html` with context:
            - `upcoming`: queryset of up to three future `Show` objects,
              ordered by date ascending.
    """
    today = timezone.localdate()  # timezone-aware "today"
    upcoming = Show.objects.filter(date__gte=today).order_by("date")[:3]
    return render(request, "band/home.html", {"upcoming": upcoming})


def about(request: HttpRequest) -> HttpResponse:
    """Render the About page with a list of band members.

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse: Renders `band/about.html` with context:
            - `members`: all `BandMember` objects ordered by name.
    """
    members = BandMember.objects.order_by("name")
    return render(request, "band/about.html", {"members": members})


class ShowList(ListView):
    """List all shows, ordered by date.

    Template:
        `band/shows.html`

    Context:
        shows (QuerySet[Show]): Shows ordered by date (ascending).
    """

    model = Show
    template_name = "band/shows.html"
    context_object_name = "shows"
    ordering = ["date"]
    paginate_by = 20  # optional; remove if you don't want pagination

    # If you want ONLY upcoming shows on this page, uncomment this:
    # def get_queryset(self):
    #     return Show.objects.filter(
    #         date__gte=timezone.localdate()
    #     ).order_by("date")


class SignUp(CreateView):
    """User signup view using Django’s built-in `UserCreationForm`."""
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
