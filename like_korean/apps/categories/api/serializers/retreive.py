# Serializers
from like_korean.apps.categories.models.index import Category

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section
class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'eng_name', 'is_active')
