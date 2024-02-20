# Serializers
from rest_framework.fields import CharField

from like_korean.apps.nationalities.models import Nationality

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section
class NationalityListSerializer(ModelSerializer):
    imageUrl = CharField(source='image_url')
    engName = CharField(source='eng_name')
    class Meta:
        model = Nationality
        fields = ('id', 'engName', 'imageUrl')
