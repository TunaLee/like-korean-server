from like_korean.apps.level_tests.models.index import TestResult
from like_korean.bases.api.serializers import ModelSerializer


class TestResultRetrieveSerializer(ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('id',)
