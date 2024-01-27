from django.urls import path

from like_korean.apps.users.api.views import UserViewSet

app_name = "users"
urlpatterns = [
    # path('login', UserViewSet.as_view({'post': 'login'})),
    # path('signup', UserViewSet.as_view({'post': 'signup'})),
]
