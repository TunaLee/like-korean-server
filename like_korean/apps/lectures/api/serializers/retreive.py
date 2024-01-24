# Serializers
from han_duck.apps.categories.models.index import Category

# Models
from han_duck.bases.api.serializers import ModelSerializer


# Class Section
class LectureRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'price', '', 'is_active')
