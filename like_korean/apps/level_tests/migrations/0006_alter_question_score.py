# Generated by Django 3.2.16 on 2024-02-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_tests', '0005_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='점수'),
        ),
    ]
