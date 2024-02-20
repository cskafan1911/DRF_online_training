from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer
from materials.validators import course_url_validator


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Course, выводит список курсов.
    """
    lessons_this_course_count = SerializerMethodField()
    lessons_this_course = SerializerMethodField()
    description = serializers.CharField(validators=[course_url_validator])

    def get_lessons_this_course_count(self, course):
        """
        Метод получает количество уроков в курсе.
        """
        return Lesson.objects.filter(course_lesson=course).count()

    def get_lessons_this_course(self, course):
        """
        Метод получает список уроков курса.
        """
        return LessonSerializer(Lesson.objects.filter(course_lesson=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'

