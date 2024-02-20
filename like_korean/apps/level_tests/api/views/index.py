# Django
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from like_korean.apps.level_tests.api.serializers.create import TestResultCreateSerializer, TestResultResponseSerializer
# Local
from like_korean.apps.level_tests.api.serializers.list import TestListSerializer, TestCategoryListSerializer, \
    LevelTestListSerializer, SolvingListSerializer, QuestionListSerializer
from like_korean.apps.level_tests.api.serializers.retrieve import TestResultRetrieveSerializer, TestRetrieveSerializer
from like_korean.apps.level_tests.api.views.filters.test import TestFilter, QuestionFilter
from like_korean.apps.level_tests.models.index import Test, TestResult, TestCategory, Solving, Question
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
    permission_classes = [IsAuthenticated]

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
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        name = request.data.get('testName')
        test = Test.objects.get(name=name)
        questions = test.questions.all().order_by('id')
        results = request.data.get('resultData')
        if len(questions) != len(results):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('error'),
            )
        total_score = 0
        solved_questions = []
        for question, result in zip(questions, results):
            is_solved = question.answer == str(result)
            total_score += question.score if is_solved else 0
            solved_questions.append(Solving(test=test, question=question, is_solved=is_solved, user=user))

        test_result = TestResult.objects.create(test=test, score=total_score)
        Solving.objects.bulk_create(solved_questions)

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


class SolvingViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializers = {
        'default': SolvingListSerializer,
    }
    permission_classes = [IsAuthenticated]
    queryset = Solving.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Solving.objects.filter(user=self.request.user)
        return queryset

    @swagger_auto_schema(**list_decorator(title=_('푼 문제 목록'), serializer=SolvingListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class QuestionViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializers = {
        'default': QuestionListSerializer
    }
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = QuestionFilter

    @swagger_auto_schema(**list_decorator(title=_('문제 목록'), serializer=QuestionListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
