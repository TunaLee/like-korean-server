from django.contrib import admin

from like_korean.apps.level_tests.models import Test, Question, Choice, Answer, QuestionImage, QuestionAudio
from like_korean.bases.admin import Admin
from like_korean.bases.inlines import StackedInline


class QuestionImageInline(StackedInline):
    model = QuestionImage
    fieldsets = (
        ("QuestionImage", {"fields": ('image',)}),
    )
    extra = 0


class QuestionAudioInline(StackedInline):
    model = QuestionAudio
    fieldsets = (
        ("QuestionAudio", {"fields": ('audio',)}),
    )
    extra = 0


class ChoiceInline(StackedInline):
    model = Choice
    fieldsets = (
        ("Choice", {"fields": ('choice', 'is_correct')}),
    )
    extra = 0


class AnswerInline(StackedInline):
    model = Answer
    fieldsets = (
        ("Answer", {"fields": ('answer',)}),
    )
    extra = 0


@admin.register(QuestionImage)
class QuestionImageAdmin(Admin):
    list_display = ('question__question_text',)
    search_fields = ('question__question_text__icontains',)

    fieldsets = (
        ("정보", {"fields": ('image',)}),
    )
    add_fieldsets = (
        ("정보", {"fields": ('image',)}),
    )


@admin.register(QuestionAudio)
class QuestionAudioAdmin(Admin):
    list_display = ('question__question_text',)
    search_fields = ('question__question_text__icontains',)

    fieldsets = (
        ("정보", {"fields": ('audio',)}),
    )
    add_fieldsets = (
        ("정보", {"fields": ('audio',)}),
    )


@admin.register(Answer)
class AnswerAdmin(Admin):
    list_display = ('question__question_text', 'answer')
    search_fields = ('question__question_text__icontains', 'answer__icontains')

    fieldsets = (
        ("정보", {"fields": ('answer',)}),
    )
    add_fieldsets = (
        ("정보", {"fields": ('answer',)}),
    )


@admin.register(Choice)
class ChoiceAdmin(Admin):
    list_display = ('question__question_text', 'choice', 'is_correct')
    search_fields = ('question__question_text__icontains', 'choice__icontains')

    fieldsets = (
        ("정보", {"fields": ('choice', 'is_correct')}),
    )
    add_fieldsets = (
        ("정보", {"fields": ('choice', 'is_correct')}),
    )


@admin.register(Question)
class QuestionView(Admin):
    list_display = ('test__name', 'question_no', 'question_text', 'is_multiple_choice', 'is_image', 'score', 'difficulty', 'category')
    search_fields = ('test__name__icontains', 'question_no', 'question_text__icontains', 'score', 'difficulty', 'category')
    inlines = (ChoiceInline, AnswerInline, QuestionImageInline, QuestionAudioInline)

    fieldsets = (
        ("정보", {"fields": ('test', 'question_no', 'question_text', 'is_multiple_choice', 'is_image', 'score', 'difficulty', 'category')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('test', 'question_no', 'question_text', 'is_multiple_choice', 'is_image', 'score', 'difficulty', 'category')}),
    )


@admin.register(Test)
class TestView(Admin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        ("정보", {"fields": ('name',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name',)}),
    )
