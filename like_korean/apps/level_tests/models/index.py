# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

from like_korean.bases.models import Model


# Local

class Test(Model):
    name = models.TextField(_('시험명'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Test')
        db_table = 'tests'
        ordering = ['-created']


class Question(Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question_no = models.IntegerField(_('문제 번호'), null=True, blank=True)
    question_text = models.TextField(_('문항'), null=True, blank=True)
    is_multiple_choice = models.BooleanField(_('객관식 여부'), default=False)
    is_image = models.BooleanField(_('이미지 여부'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('템플릿')
        db_table = 'questions'
        ordering = ['-created']


class Choice(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice = models.TextField(_('선택지'), null=False, blank=False)
    is_correct = models.BooleanField(_('정답 여부'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('객관식')
        db_table = 'choices'
        ordering = ['-created']


class Answer(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField(_('정답'), null=False, blank=False)

    class Meta:
        verbose_name = verbose_name_plural = _('주관식')
        db_table = 'answers'
        ordering = ['-created']


class QuestionImage(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_images')
    image = models.ImageField(_('이미지'), null=True, blank=True)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('문제 이미지')
        db_table = 'question_images'
        ordering = ['-created']
