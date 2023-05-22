from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from authentication.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated)

    def get_queryset(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)