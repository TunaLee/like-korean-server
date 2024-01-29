# Django
import django_filters
from django_filters import CharFilter

# Models
from like_korean.apps.level_tests.models.index import Test


class TestFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name')
    difficulty = CharFilter(field_name='questions__difficulty')
    score = CharFilter(field_name='questions__score')

    class Meta:
        model = Test
        fields = ['name', 'difficulty', 'score']
