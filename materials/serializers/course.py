from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseListSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Course, выводит список курсов.
    """

    class Meta:
        model = Course
        fields = ('name',)


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Course, выводит всю информацию о курсе.
    """
    lessons_this_course = SerializerMethodField()

    def get_lessons_this_course(self, course):
        """
        Метод получает количество уроков в курсе.
        """
        return Lesson.objects.filter(course_lesson=course).count()

    class Meta:
        model = Course
        fields = ('name', 'lessons_this_course',)
