# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from template.apps.pins.models.index import ClubPin


# Class Section
class ClubPinModelMixin(models.Model):
    club_pin_count = models.IntegerField(_('클럽 핀 수'), default=0)

    class Meta:
        abstract = True

    def pin_club(self, club):
        club_pin, created = ClubPin.objects.get_or_create(user=self, club=club)
        if not created:
            club_pin.is_active = True
            club_pin.save()
        return club_pin

    def update_user_club_pin_count(self):
        self.club_pin_count = self.club_pins.filter(is_active=True).count()
