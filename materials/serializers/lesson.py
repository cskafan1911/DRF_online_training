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
