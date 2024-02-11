from rest_framework import routers

from users.apps import UsersConfig
from users.views.payment import PaymentViewSet
from users.views.user import UserViewSet

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register('payment', PaymentViewSet, basename='payment')
router.register('users', UserViewSet, basename='user')

urlpatterns = [] + router.urls
