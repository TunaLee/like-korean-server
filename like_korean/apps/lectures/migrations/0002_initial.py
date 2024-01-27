# Generated by Django 3.2.16 on 2024-01-11 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectures', '0001_initial'),
        ('categories', '0001_initial'),
        ('languages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecturevideo',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_videos', to='lectures.lecture', verbose_name='강의'),
        ),
        migrations.AddField(
            model_name='lecturevideo',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_videos', to='lectures.unit', verbose_name='단원'),
        ),
        migrations.AddField(
            model_name='lectureimage',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_images', to='lectures.lecture', verbose_name='강의'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to='categories.category'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to='languages.language'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to=settings.AUTH_USER_MODEL),
        ),
    ]