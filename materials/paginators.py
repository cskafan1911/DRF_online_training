from rest_framework.pagination import PageNumberPagination


class MaterialsPaginator(PageNumberPagination):
    """
    Класс для пагинации вывода списка курсов или уроков.
    """

    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10