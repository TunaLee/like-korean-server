from rest_framework import serializers

from like_korean.apps.level_tests.api.serializers.list import QuestionListSerializer
from like_korean.apps.level_tests.models.index import TestResult, Test
from like_korean.bases.api.serializers import ModelSerializer


class TestRetrieveSerializer(ModelSerializer):
    questionData = serializers.SerializerMethodField()
    totalQuestion = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ('id', 'name', 'questionData', 'totalQuestion')

    def get_questionData(self, obj):
        return QuestionListSerializer(instance=obj.questions.all().order_by('question_no'), many=True).data

    def get_totalQuestion(self, obj):
        return obj.questions.filter(is_active=True).count()


class TestResultRetrieveSerializer(ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('id',)
