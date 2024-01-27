# Django
from django.db import models

# Models
from template.apps.shares.models.index import PostShare


# Class Section
class PostShareModelMixin(models.Model):
    class Meta:
        abstract = True

    def share_post(self, post, link):
        return PostShare.objects.create(user=self, post=post, link=link)
