from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """
    Класс курса.
    """

    name = models.CharField(max_length=100, verbose_name='Название курса')
    photo = models.ImageField(upload_to='course_photo/', verbose_name='Фото', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        """
        Строковое представление модели Course.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
    Класс для урока.
    """

    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='lesson_photo', verbose_name='Фото', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)

    course_lesson = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_lesson',
                                      verbose_name='Курс', null=True)

    def __str__(self):
        """
        Строковое представление модели Lesson.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
