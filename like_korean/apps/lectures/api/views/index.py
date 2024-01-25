# Django
from django.utils.translation import gettext_lazy as _
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from like_korean.apps.lectures.api.serializers.retreive import LectureRetrieveSerializer, \
    LectureVideoRetrieveSerializer, UnitRetrieveSerializer
from like_korean.apps.lectures.api.views.filters.lecture_filter import UnitsFilter
from like_korean.apps.lectures.models.index import Lecture, LectureVideo
from like_korean.bases.api import mixins
from like_korean.utils.decorators import retrieve_decorator


# Class Section
class LectureViewSet(mixins.RetrieveModelMixin):
    serializers = {
        'default': LectureRetrieveSerializer,
    }
    queryset = Lecture.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**retrieve_decorator(title=_('강좌'), serializer=LectureRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


class UnitViewSet(mixins.RetrieveModelMixin):
    serializer_class = {
        'default': UnitRetrieveSerializer
    }
    queryset = LectureVideo.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = UnitsFilter
    @swagger_auto_schema(**retrieve_decorator(title=_('강의 영상'), serializer=LectureVideoRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)
