from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import EmailField, CharField, ValidationError
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = EmailField(required=True, validators = [UniqueValidator(queryset=User.objects.all())])
    password = CharField(write_only=True, validators=[validate_password])
    confirm_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_passord']