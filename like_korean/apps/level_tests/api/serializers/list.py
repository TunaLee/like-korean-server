# Serializers
from rest_framework import serializers
from rest_framework.fields import IntegerField, CharField, BooleanField, FloatField

from like_korean.apps.level_tests.models.index import Test, QuestionImage, Choice, Answer, Question

# Models
from like_korean.bases.api.serializers import ModelSerializer


# Class Section

class QuestionImageSerializer(ModelSerializer):
    imageUrl = CharField(source='image_url')

    class Meta:
        model = QuestionImage
        fields = ('imageUrl',)


class AnswerListSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer',)


class ChoiceListSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice',)


class QuestionListSerializer(ModelSerializer):
    questionNo = IntegerField(source='question_no')
    questionText = CharField(source='question_text')
    imageUrl = CharField(source='image_url')
    audioUrl = CharField(source='audio_url')
    isImage = BooleanField(source='is_image')
    isAudio = BooleanField(source='is_audio')
    isMultipleChoice = BooleanField(source='is_multiple_choice')
    choiceData = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('questionNo', 'questionText', 'imageUrl', 'audioUrl', 'imageUrl', 'audioUrl', 'isImage', 'isAudio',
                  'isMultipleChoice', 'choiceData')

    def get_choiceData(self, obj):
        return ChoiceListSerializer(instance=obj.choices, many=True).data


class TestListSerializer(ModelSerializer):
    questionData = serializers.SerializerMethodField()
    totalQuestion = serializers.SerializerMethodField()
    attemptCount = IntegerField(source='attempt_count')
    avgScore = FloatField(source='avg_score')

    class Meta:
        model = Test
        fields = ('name', 'questionData', 'totalQuestion', 'attemptCount', 'avgScore')

    def get_questionData(self, obj):
        return QuestionListSerializer(instance=obj.questions.all().order_by('question_no'), many=True).data

    def get_totalQuestion(self, obj):
        return obj.questions.filter(is_active=True).count()
