# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter

from like_korean.apps.level_tests.api.serializers.create import TestResultCreateSerializer, TestResultResponseSerializer
# Local
from like_korean.apps.level_tests.api.serializers.list import TestListSerializer, TestCategoryListSerializer, \
    LevelTestListSerializer
from like_korean.apps.level_tests.api.serializers.retrieve import TestResultRetrieveSerializer, TestRetrieveSerializer
from like_korean.apps.level_tests.api.views.filters.test import TestFilter
from like_korean.apps.level_tests.models.index import Test, TestResult, TestCategory
from like_korean.bases.api import mixins
from like_korean.bases.api.viewsets import GenericViewSet
from like_korean.utils.api.response import Response
from like_korean.utils.decorators import list_decorator, create_decorator, retrieve_decorator


# Class Section
class LevelTestViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializers = {
        'default': LevelTestListSerializer
    }
    queryset = Test.objects.filter(name='level test')
    filter_backends = (DjangoFilterBackend,)
    filter_class = TestFilter

    @swagger_auto_schema(**list_decorator(title=_('레벨 테스트 문제 목록'), serializer=TestListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class TestViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializers = {
        'default': TestListSerializer,
        'retrieve': TestRetrieveSerializer
    }
    queryset = Test.objects.filter(name__icontains='EPSTOPIK')
    filter_backends = (DjangoFilterBackend,)
    filter_class = TestFilter

    @swagger_auto_schema(**list_decorator(title=_('문제 목록'), serializer=TestListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @swagger_auto_schema(**retrieve_decorator(title=_('문제 상세 조회'), serializer=TestRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

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
        name = request.data.get('testName')
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


class TestCategoryViewSet(
    GenericViewSet,
    mixins.ListModelMixin
):
    queryset = TestCategory.objects.all()
    serializers = {
        'default': TestCategoryListSerializer
    }

    @swagger_auto_schema(**list_decorator(title=_('테스트 카테고리 목록'), serializer=TestCategoryListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

