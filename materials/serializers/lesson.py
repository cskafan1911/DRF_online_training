from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Lesson.
    """

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для списка уроков.
    """
    course_lesson = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для списка уроков.
    """

    course_lesson = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
