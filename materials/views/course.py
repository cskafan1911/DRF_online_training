from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.permissions import IsUserIsOwner, IsModerator
from materials.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    """
    Класс ViewSet для модели Course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        """
        Метод ограничивает права доступа.
        """
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator, IsUserIsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsUserIsOwner]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """
        Метод для привязки создателя и курса.
        """
        course = serializer.save()
        course.owner = self.request.user
        course.save()
