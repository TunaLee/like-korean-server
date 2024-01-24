# Manager
from superclub.apps.likes.models.managers.objects import PostLikeMainManager


# Class Section
class PostLikeActiveManager(PostLikeMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
