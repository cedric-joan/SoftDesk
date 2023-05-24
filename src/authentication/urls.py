from rest_framework import routers
from authentication.views import UsersViewSet

router = routers.SimpleRouter()
router.register('signup', UsersViewSet, basename='signup'),
