# Local
from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import CharField, EmailField
from rest_framework.validators import UniqueValidator

from like_korean.apps.users.models import User
from like_korean.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class UserSignUpSerializer(ModelSerializer):
    email = EmailField(required=True, write_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(required=True, write_only=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'nationality')

class UserSignInSerializer(ModelSerializer):
    email = EmailField(required=True)
    password = CharField(required=True, write_only=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('email', 'password')
