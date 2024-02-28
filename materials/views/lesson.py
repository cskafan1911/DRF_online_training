from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.paginators import MaterialsPaginator
from materials.permissions import IsModerator, IsUserIsOwner
from materials.serializers.lesson import LessonSerializer


class LessonListView(ListAPIView):
    """
    Класс для получения списка уроков.
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPaginator
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]


class LessonDetailView(RetrieveAPIView):
    """
    Класс для просмотра одного урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]


class LessonCreateView(CreateAPIView):
    """
    Класс для создания урока.
    """

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """
        Метод для привязки создателя и урока.
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


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
