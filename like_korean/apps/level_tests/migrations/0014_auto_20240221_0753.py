# Generated by Django 3.2.16 on 2024-02-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_tests', '0013_auto_20240221_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='attempt_count',
            field=models.IntegerField(default=0, verbose_name='응시 횟수'),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_count',
            field=models.IntegerField(default=0, verbose_name='정답 횟수'),
        ),
    ]
