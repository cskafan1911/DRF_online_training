from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Lesson
from materials.serializers.lesson import LessonSerializer


class LessonListView(ListAPIView):
    """
    Класс для получения списка уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(RetrieveAPIView):
    """
    Класс для просмотра одного урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateView(CreateAPIView):
    """
    Класс для создания урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateView(UpdateAPIView):
    """
    Класс для редактирования урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteView(DestroyAPIView):
    """
    Класс для удаления урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
