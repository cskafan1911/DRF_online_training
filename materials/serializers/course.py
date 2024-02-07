from rest_framework import serializers

from materials.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Course.
    """

    class Meta:
        model = Course
        fields = '__all__'
