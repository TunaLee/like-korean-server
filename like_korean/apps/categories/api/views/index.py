# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from like_korean.apps.categories.api.serializers.retreive import CategoryRetrieveSerializer
from like_korean.apps.categories.models.index import Category
from like_korean.bases.api import mixins
from like_korean.utils.decorators import retrieve_decorator


# Class Section
class CategoryViewSet(mixins.RetrieveModelMixin):
    serializers = {
        'default': CategoryRetrieveSerializer,
    }
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**retrieve_decorator(title=_('강좌 카테고리 - Guest'), serializer=CategoryRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)
