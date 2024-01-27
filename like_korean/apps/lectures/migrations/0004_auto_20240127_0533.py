# Generated by Django 3.2.16 on 2024-01-27 05:33

from django.db import migrations, models
import like_korean.apps.lectures.models.index


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20240113_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectureimage',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=like_korean.apps.lectures.models.index.detail_thumbnail_image_path, verbose_name='썸네일 이미지'),
        ),
        migrations.AlterField(
            model_name='lecturevideo',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=like_korean.apps.lectures.models.index.video_thumbnail_image_path, verbose_name='썸네일 이미지'),
        ),
        migrations.AlterField(
            model_name='lecturevideo',
            name='video',
            field=models.FileField(upload_to=like_korean.apps.lectures.models.index.lecture_video_path, verbose_name='비디오'),
        ),
    ]
