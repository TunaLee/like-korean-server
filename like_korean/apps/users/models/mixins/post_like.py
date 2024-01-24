# Django
from django.db import models

# Models
from template.apps.likes.models import PostLike, PostDislike


# Class Section
class PostLikeModelMixin(models.Model):
    class Meta:
        abstract = True

    def like_post(self, post, profile):
        post_dislike = post.post_dislikes.filter(profile=profile).first()
        if post_dislike:
            post_dislike.is_active = False
            post_dislike.save()
        post_like, created = PostLike.objects.get_or_create(user=self, post=post, profile=profile)
        if not created:
            post_like.is_active = True
            post_like.save()
        return post_like

    def dislike_post(self, post, profile):
        post_like = post.post_likes.filter(profile=profile).first()
        if post_like:
            post_like.is_active = False
            post_like.save()
        post_dislike, created = PostDislike.objects.get_or_create(user=self, post=post, profile=profile)
        if not created:
            post_dislike.is_active = True
            post_dislike.save()
        return post_dislike
