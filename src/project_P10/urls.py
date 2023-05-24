from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from softDesk.urls import router as softDesk_router
from authentication.urls import router as authentication_router

router = routers.SimpleRouter()
router.registry.extend(softDesk_router.registry)
router.registry.extend(authentication_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
