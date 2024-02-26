from django_filters import Filter


class ListFilter(Filter):
    def filter(self, qs, value):

        if value:
            value_list = value.split(',')
            return qs.filter(**{f'{self.field_name}__in': value_list})
        return qs
