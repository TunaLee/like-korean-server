# Serializers
from like_korean.apps.lectures.models.index import LectureVideo, Lecture, Unit
from like_korean.apps.level_test.models.index import Test, QuestionImage, Choice, Answer, Question

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section

class QuestionImageSerializer(ModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ('image_url',)
class AnswerListSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer',)

class ChoiceListSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = ('choice', )


class QuestionListSerializer(ModelSerializer):
    question_images = QuestionImageSerializer(many=True, read_only=True)
    answers = AnswerListSerializer(many=True, read_only=True)
    choices = ChoiceListSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('question_no', 'question_text', 'question_images', 'answers', 'choices')


class TestListSerializer(ModelSerializer):
    quests = QuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('name', 'quests')
