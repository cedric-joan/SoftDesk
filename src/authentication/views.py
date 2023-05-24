from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from authentication.serializers import UserSerializer


class UsersViewSet(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = (AllowAny)

    def get_queryset(self):
        return User.objects.all()