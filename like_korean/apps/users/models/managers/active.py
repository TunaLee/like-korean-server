# Manager
from template.apps.users.models.managers.objects import UserMainManager


# Class Section
class UserActiveManager(UserMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
