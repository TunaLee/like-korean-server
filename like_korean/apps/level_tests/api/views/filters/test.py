# Django
import django_filters
from django_filters import CharFilter

# Models
from like_korean.apps.level_test.models.index import Test


class QuestionFilter(django_filters.FilterSet):
    name = CharFilter(field_name='test__name')

    class Meta:
        model = Test
        fields = ['name']
