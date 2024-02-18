from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Метод для регистрации нового пользователя.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Класс для просмотра пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserListAPIView(generics.ListAPIView):
    """
    Класс для просмотра пользователей.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для редактирования пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
