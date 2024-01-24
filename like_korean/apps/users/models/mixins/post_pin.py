# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from template.apps.pins.models.index import PostPin


# Class Section
class PostPinModelMixin(models.Model):
    post_pin_count = models.IntegerField(_('게시글 핀 수'), default=0)

    class Meta:
        abstract = True

    def pin_post(self, post):
        post_pin, created = PostPin.objects.get_or_create(user=self, post=post)
        if not created:
            post_pin.is_active = True
            post_pin.save()
        return post_pin

    def update_user_post_pin_count(self):
        self.post_pin_count = self.post_pins.filter(is_active=True).count()
