# Django
import os
from time import strftime, gmtime

from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.apps.users.forms import User
from like_korean.bases.models import Model


def file_path(path, filename):
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(path, filename)


def question_audio_path(instance, filename):
    return file_path('Question/Audio/', filename)


def question_image_path(instance, filename):
    return file_path('Question/Image/', filename)


class Test(Model):
    name = models.TextField(_('시험명'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Test')
        db_table = 'tests'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Question(Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question_no = models.IntegerField(_('문제 번호'), null=True, blank=True)
    question_text = models.TextField(_('문항'), null=True, blank=True)
    image_url = models.TextField(_('이미지 url'), null=True, blank=True)
    audio_url = models.TextField(_('오디오 url'), null=True, blank=True)
    answer = models.TextField(_('정답'), null=True, blank=True)
    score = models.PositiveSmallIntegerField(_('점수'), default=0)

    is_multiple_choice = models.BooleanField(_('객관식 여부'), default=True)
    is_image = models.BooleanField(_('이미지 여부'), default=False)
    is_audio = models.BooleanField(_('오디오 여부'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('문항')
        db_table = 'questions'
        ordering = ['-created']


class Choice(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice = models.TextField(_('선택지'), null=False, blank=False)
    is_correct = models.BooleanField(_('정답 여부'), default=False)

    def save(self, *args, **kwargs):
        if self.question:
            if self.is_correct:
                self.question.answer = self.choice
            self.question.is_multiple_choice = True
            self.question.save()
        super(Choice, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        if self.question:
            self.question.answer = self.answer
            self.question.is_multiple_choice = False
            self.question.save()


class QuestionAudio(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_audios')
    audio = models.FileField(_('오디오'), upload_to=question_audio_path)
    audio_url = models.URLField(_('오디오 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('문제 오디오')
        db_table = 'question_audios'
        ordering = ['-created']


class QuestionImage(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_images')
    image = models.ImageField(_('이미지'), upload_to=question_image_path)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('문제 이미지')
        db_table = 'question_images'
        ordering = ['-created']


class TestResult(Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_results')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results', null=True, blank=True)
    score = models.IntegerField(_('점수'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('시험 결과')
        db_table = 'test_results'
        ordering = ['-created']
