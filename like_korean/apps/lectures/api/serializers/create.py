# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.boards.models import BoardGroup, Board


# Class Section
class BoardGroupCreateSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('name', 'is_active')


class BoardCreateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'description', 'view_mode', 'read_permission', 'write_permission', 'is_active')
