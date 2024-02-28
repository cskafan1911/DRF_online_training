from rest_framework import serializers

from materials.models import Lesson
from materials.validators import LessonUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Lesson.
    """

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LessonUrlValidator(field='video_url')
        ]
