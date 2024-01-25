# Serializers
from like_korean.apps.categories.models.index import Category
from like_korean.apps.lectures.models.index import LectureVideo, Lecture, Unit

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section
class LectureRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'name', 'description', 'price', 'is_active')


class LectureVideoRetrieveSerializer(ModelSerializer):

    class Meta:
        model = LectureVideo
        fields = ('id', 'name', 'description', 'video_url', 'lecture', 'thumbnail_image_url', 'is_active')


class UnitRetrieveSerializer(ModelSerializer):
    lecture_videos = LectureVideoRetrieveSerializer(many=True)
    class Meta:
        model = Unit
        fields = ('id', 'name', 'description', 'lecture_videos', 'is_active')
