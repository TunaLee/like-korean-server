# Local
from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import CharField, EmailField, IntegerField, SerializerMethodField
from rest_framework.validators import UniqueValidator

from like_korean.apps.users.models import User
from like_korean.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    nationalityName = CharField(source='nationality.eng_name', required=False)
    nationalityImageUrl = CharField(source='nationality.image_url', required=False)
    totalSolved = IntegerField(source='total_solved')
    correctSolved = IntegerField(source='correct_solved')

    class Meta:
        model = User
        fields = ('username', 'nationalityName', 'nationalityImageUrl', 'totalSolved', 'correctSolved')


class UserValidateEmailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class UserMeSerializer(ModelSerializer):
    nationalityName = CharField(source='nationality.eng_name')
    nationalityImageUrl = CharField(source='nationality.image_url')
    totalSolved = IntegerField(source='total_solved')
    correctSolved = IntegerField(source='correct_solved')
    rank = SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'nationalityName', 'nationalityImageUrl', 'totalSolved', 'correctSolved', 'rank')

    def get_rank(self, obj):
        return User.objects.filter(correct_solved__gt=obj.correct_solved).count() + 1


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
