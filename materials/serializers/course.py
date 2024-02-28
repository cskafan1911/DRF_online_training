from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer
from materials.validators import course_url_validator
from subscriptions.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Course, выводит список курсов.
    """
    lessons_this_course_count = SerializerMethodField()
    lessons_this_course = SerializerMethodField()
    description = serializers.CharField(validators=[course_url_validator])
    subscription = serializers.SerializerMethodField()

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

    def get_subscription(self, instance):
        """
        Метод получает информацию о подписке пользователя.
        """
        return Subscription.objects.filter(course=instance, user=self.context['request'].user).exists()

    class Meta:
        model = Course
        fields = '__all__'
