# Serializers
from han_duck.apps.categories.models.index import Category

# Models
from han_duck.bases.api.serializers import ModelSerializer


# Class Section
class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'eng_name', 'is_active')
