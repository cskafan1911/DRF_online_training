from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers.course import CourseDetailSerializer


class CourseViewSet(ModelViewSet):
    """
    Класс ViewSet для модели Course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
