# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter

from like_korean.apps.level_tests.api.serializers.create import TestResultCreateSerializer, TestResultResponseSerializer
# Local
from like_korean.apps.level_tests.api.serializers.list import TestListSerializer
from like_korean.apps.level_tests.api.serializers.retrieve import TestResultRetrieveSerializer
from like_korean.apps.level_tests.api.views.filters.test import TestFilter
from like_korean.apps.level_tests.models.index import Question, Test, TestResult
from like_korean.bases.api import mixins
from like_korean.bases.api.viewsets import GenericViewSet
from like_korean.utils.api.response import Response
from like_korean.utils.decorators import list_decorator, create_decorator, retrieve_decorator


# Class Section
class TestViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializers = {
        'default': TestListSerializer
    }
    queryset = Test.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = TestFilter

    @swagger_auto_schema(**list_decorator(title=_('문제 목록'), serializer=TestListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class TestResultViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = TestResult.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    serializers = {
        'default': TestResultRetrieveSerializer,
        'create': TestResultCreateSerializer
    }

    @swagger_auto_schema(**create_decorator('test-result'))
    def create(self, request, *args, **kwargs):
        name = request.data.get('testName')['name']
        test = Test.objects.get(name=name)
        questions = test.questions.all()
        results = request.data.get('resultData')
        if len(questions) != len(results):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('error'),
            )

        total_score = sum(
            question.score for question, result in zip(questions, results) if question.answer == result
        )
        test_result = TestResult.objects.create(test=test, score=total_score)

        return Response(
            status=status.HTTP_200_OK,
            code=200,
            data=TestResultResponseSerializer(instance=test_result).data,
            message=_('ok')
        )

    @swagger_auto_schema(**retrieve_decorator('test-result'))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            data=TestResultResponseSerializer(instance=instance).data,
            message=_('ok')
        )

