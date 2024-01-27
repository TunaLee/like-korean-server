# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.boards.models import Board
from superclub.apps.boards.models import BoardGroup


# Class Section
class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'type', 'order', 'is_active')


class BoardGroupListSerializer(ModelSerializer):
    boards = BoardListSerializer(read_only=True, many=True)

    class Meta:
        model = BoardGroup
        fields = ('id', 'name', 'type', 'order', 'is_active', 'boards')
