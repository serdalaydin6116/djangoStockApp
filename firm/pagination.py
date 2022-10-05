from rest_framework.pagination import PageNumberPagination



class SmallPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_query_param = "sheet"

