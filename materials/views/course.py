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
        Метод для
        """
        if self.action in ['create', 'retrieve_delete']:
            self.permission_classes = [IsAuthenticated, IsUserIsOwner, IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsUserIsOwner | IsModerator]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.queryset.filter(owner=self.request.user).exists():
            return Course.objects.filter(owner=self.request.user)
        elif self.request.user.is_superuser or self.request.user.groups.filter(name='moderator').exists():
            return self.queryset
