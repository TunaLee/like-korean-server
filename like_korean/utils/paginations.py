from django.http import JsonResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return JsonResponse({'code': 200,
                             'message': 'ok',
                             'count': self.page.paginator.count,
                             'next': self.get_next_link(),
                             'previous': self.get_previous_link(),
                             'data': data},
                            status=status.HTTP_200_OK)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000
