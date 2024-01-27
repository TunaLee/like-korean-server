# Serializers
from rest_framework import serializers
from rest_framework.fields import ListField, CharField

from like_korean.apps.level_tests.models.index import TestResult
from like_korean.bases.api.serializers import ModelSerializer


# Models


# Class Section
class TestResultCreateSerializer(ModelSerializer):
    name = serializers.SerializerMethodField()
    resultData = ListField(child=CharField())

    class Meta:
        model = TestResult
        fields = ('name', 'resultData')

    def get_name(self, obj):
        return obj.tests.name

class TestResultResponseSerializer(ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('score',)
