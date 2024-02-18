# Serializers
from rest_framework.fields import CharField

from like_korean.apps.nationalities.models import Nationality

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section
class NationalityListSerializer(ModelSerializer):
    imageUrl = CharField(source='image_url')
    class Meta:
        model = Nationality
        fields = ('id', 'name', 'imageUrl')
