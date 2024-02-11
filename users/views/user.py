from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Класс ViewSet для модели Payment
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
