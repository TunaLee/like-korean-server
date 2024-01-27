# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from template.apps.joins.models.index import Join


# Class Section
class JoinModelMixin(models.Model):
    join_count = models.IntegerField(_('가입 수'), default=0)

    class Meta:
        abstract = True

    def join_club(self, club):
        join, created = Join.objects.get_or_create(club=club, user=self)
        if not created:
            join.is_active = True
            join.save()
        return join

    def update_user_join_count(self):
        self.join_count = self.joins.filter(is_active=True).count()
