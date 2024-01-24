# Django
from django.db import models

# Models
from template.apps.likes.models import CommentLike, CommentDislike


# Class Section
class CommentLikeModelMixin(models.Model):
    class Meta:
        abstract = True

    def like_comment(self, comment, profile):
        comment_dislike = comment.comment_dislikes.filter(profile=profile).first()
        if comment_dislike:
            comment_dislike.is_active = False
            comment_dislike.save()
        comment_like, created = CommentLike.objects.get_or_create(user=self, comment=comment, profile=profile)
        if not created:
            comment_like.is_active = True
            comment_like.save()
        return comment_like

    def dislike_comment(self, comment, profile):
        comment_like = comment.comment_likes.filter(profile=profile).first()
        if comment_like:
            comment_like.is_active = False
            comment_like.save()
        comment_dislike, created = CommentDislike.objects.get_or_create(user=self, comment=comment, profile=profile)
        if not created:
            comment_dislike.is_active = True
            comment_dislike.save()
        return comment_dislike
