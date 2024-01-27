# Django
import django_filters
from django_filters import CharFilter, NumberFilter, RangeFilter

from like_korean.apps.lectures.models.index import Lecture, LectureVideo


# Models

class UnitsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name')
    lecture_id = NumberFilter(field_name='lecture_id')
    is_active = CharFilter(field_name='is_active')
    class Meta:
        model = Lecture
        fields = ['name', 'lecture_id', 'is_active']

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)

class LecturesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name')
    category_id = NumberFilter(field_name='category_id')
    owner_id = NumberFilter(field_name='owner_id')
    price = RangeFilter(field_name='price')
    is_active = CharFilter(field_name='is_active')
    class Meta:
        model = Lecture
        fields = ['name', 'category_id', 'owner_id', 'price', 'is_active']

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)
