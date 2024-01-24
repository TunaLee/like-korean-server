# Django
from django.utils.translation import gettext_lazy as _
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from like_korean.apps.level_test.api.serializers.list import QuestionListSerializer
from like_korean.apps.level_test.api.views.filters.test import QuestionFilter
from like_korean.apps.level_test.models.index import Question
from like_korean.bases.api import mixins
from like_korean.utils.decorators import list_decorator


# Class Section
class QuestionViewSet(mixins.ListModelMixin):
    serializers = {
        'default': QuestionListSerializer
    }
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = QuestionFilter
    @swagger_auto_schema(**list_decorator(title=_('문제 목록'), serializer=QuestionListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
