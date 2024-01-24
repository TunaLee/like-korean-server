# Django
from django.db import models

# Models
from template.apps.shares.models.index import ClubShare


# Class Section
class ClubShareModelMixin(models.Model):
    class Meta:
        abstract = True

    def share_club(self, club, link):
        return ClubShare.objects.create(user=self, club=club, link=link)
