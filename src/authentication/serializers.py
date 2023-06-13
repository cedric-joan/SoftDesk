from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import EmailField, CharField, ValidationError, ModelSerializer
from rest_framework.validators import UniqueValidator

class SignupSerializer(ModelSerializer):
    email = EmailField(required=True, validators = [UniqueValidator(queryset=User.objects.all())])
    password = CharField(write_only=True, validators=[validate_password])
    confirm_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError({"Not matching passwords"})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user