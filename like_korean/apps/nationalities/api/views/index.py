# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from like_korean.apps.nationalities.api.serializers.list import NationalityListSerializer
from like_korean.apps.nationalities.models import Nationality
from like_korean.bases.api import mixins
from like_korean.bases.api.viewsets import GenericViewSet
from like_korean.utils.decorators import list_decorator


# Class Section
class NationalityViewSet(
    GenericViewSet,
    mixins.ListModelMixin
):
    serializers = {
        'default': NationalityListSerializer,
    }
    queryset = Nationality.objects.all().order_by('eng_name')
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**list_decorator(title=_('국가 조회'), serializer=NationalityListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
