# Serializers
from com_duck.apps.boards.models import Board
from com_duck.bases.api.serializers import ModelSerializer


# Models


# Class Section
class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
