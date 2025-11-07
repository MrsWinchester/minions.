# band/models.py
from __future__ import annotations

"""Data models for the `band` app.

Contains:
- `Show`: a scheduled performance (title, venue, city, date, optional price, sold-out flag)
- `BandMember`: a band member profile (name, role, optional bio)
"""

from django.db import models


class Show(models.Model):
    """A public performance by the band.

    Fields:
        title: Name of the show or event.
        venue: Venue where the show will take place.
        city: City of the venue.
        date: Calendar date of the performance.
        price: Ticket price (may be blank/NULL for free events).
        is_sold_out: Whether tickets are sold out.
    """

    title = models.CharField(max_length=120)
    venue = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_sold_out = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Human-readable label used in admin and the shell."""
        return f"{self.title} @ {self.venue} ({self.date})"


class BandMember(models.Model):
    """A member of the band.

    Fields:
        name: Full name of the band member.
        role: Main role in the band (e.g., Vocals, Guitar, Drums).
        bio: Optional short biography or notes.
    """

    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        """Human-readable label used in admin and the shell."""
        return f"{self.name} – {self.role}"
