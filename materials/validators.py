import re
from rest_framework.serializers import ValidationError


class LessonUrlValidator:
    """
    Класс проверки ссылок на сторонние ресурсы в модели Lesson.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'(http://|https://)?(www)?(\.?)(youtube)\.(com)/?')
        tmp_val = dict(value).get(self.field)

        if not bool(reg.match(tmp_val)):
            raise ValidationError('Можно использовать ссылки только с youtube')


def course_url_validator(text):
    """
    Функция для проверки ссылок на сторонние ресурсы в модели Course.
    """

    if '.com' or '.ru' or '.org' in text:
        if text.count('youtube.com') + text.count('youtube.ru') != text.count('.com') + text.count('.ru') + text.count(
                '.org'):
            raise ValidationError('Можно использовать ссылки только с youtube')
