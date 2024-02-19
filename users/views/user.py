from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from materials.permissions import IsUserIsOwner, IsModerator
from users.models import User, Payment
from users.serializers.payment import PaymentSerializer
from users.serializers.user import UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    Класс ViewSet для модели Payment.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date',)


class UserRegisterAPI(generics.CreateAPIView):
    """
    Класс дял создания пользователя.
    """
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """
        Метод шифрует пароль пользователя.
        """
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()


class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Класс для просмотра пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsUserIsOwner]


class UserListAPIView(generics.ListAPIView):
    """
    Класс для просмотра пользователей.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для редактирования пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserIsOwner]

    def perform_update(self, serializer):
        """
        Метод шифрует пароль пользователя.
        """
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
