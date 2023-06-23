from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from authentication.serializers import SignupSerializer


class SignupViewSet(CreateAPIView):

    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()