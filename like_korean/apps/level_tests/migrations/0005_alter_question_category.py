# Generated by Django 3.2.16 on 2024-02-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_tests', '0004_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.TextField(blank=True, choices=[('GRAMMAR', '문법'), ('READING', '읽기'), ('WRITING', '쓰기'), ('SPEAKING', '말하기'), ('LISTENING', '듣기')], null=True, verbose_name='문제 유형'),
        ),
    ]
