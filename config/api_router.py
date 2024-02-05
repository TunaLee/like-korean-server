# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

from like_korean.apps.level_tests.api.views.index import TestViewSet, TestResultViewSet, LevelTestViewSet, \
    TestCategoryViewSet
from like_korean.apps.users.api.views import UserViewSet

# users


# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)
router.register("level-test", LevelTestViewSet)
router.register("test", TestViewSet)
router.register("test-result", TestResultViewSet)
router.register("test-category", TestCategoryViewSet)
app_name = 'api'
urlpatterns = [
                  path('', include("like_korean.apps.users.urls")),
              ] + router.urls
