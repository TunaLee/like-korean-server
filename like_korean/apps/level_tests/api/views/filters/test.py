# Django
import django_filters
from django.db.models import Q
from django_filters import CharFilter, BooleanFilter, AllValuesFilter

# Models
from like_korean.apps.level_tests.models.index import Test, Question, Solving
from like_korean.utils.filters import ListFilter


class TestFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    difficulty = CharFilter(field_name='questions__difficulty')
    score = CharFilter(field_name='questions__score')
    category = CharFilter(field_name='category')

    class Meta:
        model = Test
        fields = ['name', 'difficulty', 'score', 'category']


class QuestionFilter(django_filters.FilterSet):
    category = CharFilter(method='filter_category')
    difficulty = CharFilter(method='filter_difficulty')
    # difficulty = CharFilter(field_name='difficulty')
    isSolved = CharFilter(method='filter_isSolved')

    class Meta:
        model = Question
        fields = ['difficulty', 'category', 'isSolved']

    def filter_category(self, queryset, name, value):
        if value:
            queryset = queryset.filter(category__in=value.split(','))
        return queryset

    def filter_difficulty(self, queryset, name, value):
        if value:
            queryset = queryset.filter(difficulty__in=value.split(','))
        return queryset

    def filter_isSolved(self, queryset, name, value):
        if value == 'true':
            queryset = queryset.filter(solvings__user=self.request.user).distinct()
        return queryset
