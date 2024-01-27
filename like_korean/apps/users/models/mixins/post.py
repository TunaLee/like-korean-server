# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class PostModelMixin(models.Model):
    post_count = models.IntegerField(_('게시글 수'), default=0)

    class Meta:
        abstract = True

    # TODO 로직 점검하기
    # def update_user_post_count(self):
    #     self.post_count = self.posts.filter(is_active=True).count()
