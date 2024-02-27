from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from materials.models import Course
from users.models import Payment
from users.serializers.payment import PaymentSerializer
from users.services import create_product_price, create_session


class PaymentViewSet(ModelViewSet):
    """
    Класс ViewSet для модели Payment
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):

        product = get_object_or_404(Course, pk=request.data.get('course'))

        if product:
            price = create_product_price(product.price, product.name)
            session = create_session(price)
            session_id = session.id
            session_url = session.url
            payment = Payment.objects.create(
                user=self.request.user,
                course=product,
                lesson=request.data.get('lesson'),
                payment_amount=product.price,
                session_id=session_id,
                pay_url=session_url,
            )
            payment.save()
            return Response({'payment_url': payment.pay_url}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Error! Not found!'}, status=status.HTTP_404_NOT_FOUND)
