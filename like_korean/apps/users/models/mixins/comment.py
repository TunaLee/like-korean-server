# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class CommentModelMixin(models.Model):
    comment_count = models.IntegerField(_('댓글 수'), default=0)

    class Meta:
        abstract = True

    def update_user_comment_count(self):
        self.comment_count = self.comments.filter(is_active=True).count()
