# Local
from template.apps.users.models import User
from template.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)
