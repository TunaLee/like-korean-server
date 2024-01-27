# Generated by Django 3.2.16 on 2024-01-13 19:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import like_korean.bases.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('question_no', models.IntegerField(blank=True, null=True, verbose_name='문제 번호')),
                ('question_text', models.TextField(blank=True, null=True, verbose_name='문항')),
                ('is_multiple_choice', models.BooleanField(default=False, verbose_name='객관식 여부')),
                ('is_image', models.BooleanField(default=False, verbose_name='이미지 여부')),
            ],
            options={
                'verbose_name': '템플릿',
                'verbose_name_plural': '템플릿',
                'db_table': 'questions',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('name', models.TextField(blank=True, null=True, verbose_name='시험명')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Test',
                'db_table': 'tests',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='이미지 URL')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_images', to='level_tests.question')),
            ],
            options={
                'verbose_name': '문제 이미지',
                'verbose_name_plural': '문제 이미지',
                'db_table': 'question_images',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='level_tests.test'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('choice', models.TextField(verbose_name='선택지')),
                ('is_correct', models.BooleanField(default=False, verbose_name='정답 여부')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='level_tests.question')),
            ],
            options={
                'verbose_name': '객관식',
                'verbose_name_plural': '객관식',
                'db_table': 'choices',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('answer', models.TextField(verbose_name='정답')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='level_tests.question')),
            ],
            options={
                'verbose_name': '주관식',
                'verbose_name_plural': '주관식',
                'db_table': 'answers',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
        ),
    ]