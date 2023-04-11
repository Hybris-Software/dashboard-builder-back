from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'page'
    page_size = 10
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),  # next page url
                'previous': self.get_previous_link()  # previous page url
            },
            'page': self.page.number,  # current page number
            'from': self.page.start_index(),  # start index of the current page
            'to': self.page.end_index(),  # end index of the current page
            'count': self.page.paginator.count,  # total number of items
            'results': data  # data of the current page
        }, status=status.HTTP_200_OK)
