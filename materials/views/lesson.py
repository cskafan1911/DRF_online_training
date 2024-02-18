from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.permissions import IsModerator, IsUserIsOwner
from materials.serializers.lesson import LessonSerializer, LessonListSerializer, LessonDetailSerializer


class LessonListView(ListAPIView):
    """
    Класс для получения списка уроков.
    """

    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]

    def get_queryset(self):
        if Lesson.objects.filter(owner=self.request.user).exists():
            self.serializer_class = LessonDetailSerializer
            return Lesson.objects.filter(owner=self.request.user)
        elif self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_staff:
            return Lesson.objects.all()


class LessonDetailView(RetrieveAPIView):
    """
    Класс для просмотра одного урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]


class LessonCreateView(CreateAPIView):
    """
    Класс для создания урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonUpdateView(UpdateAPIView):
    """
    Класс для редактирования урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]


class LessonDeleteView(DestroyAPIView):
    """
    Класс для удаления урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsUserIsOwner]
