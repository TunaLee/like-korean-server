# Local
from like_korean.apps.users.models import User
from like_korean.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)
