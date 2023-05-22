from rest_framework import routers
from authentication.views import UsersViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')