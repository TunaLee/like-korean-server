# Serializers
from rest_framework import serializers
from rest_framework.fields import ListField, CharField

from like_korean.apps.level_tests.models.index import TestResult, Test
from like_korean.bases.api.serializers import ModelSerializer


# Models


# Class Section

class TestResultCreateSerializer(ModelSerializer):
    testName = CharField(source='test.name', read_only=True)
    resultData = ListField(child=CharField())

    class Meta:
        model = TestResult
        fields = ('testName', 'resultData')


class TestResultResponseSerializer(ModelSerializer):
    testName = CharField(source='test.name', read_only=True)
    class Meta:
        model = TestResult
        fields = ('id', 'score', 'testName')
