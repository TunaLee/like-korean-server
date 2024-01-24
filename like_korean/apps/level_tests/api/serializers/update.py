# DRF
from rest_framework import serializers

# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.boards.models import BoardGroup, Board


# Class Section
class BoardGroupOrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('order',)


class BoardGroupMergeUpdateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = BoardGroup
        fields = ('id',)


class BoardOrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_group', 'order',)


class BoardMergeUpdateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Board
        fields = ('id',)
