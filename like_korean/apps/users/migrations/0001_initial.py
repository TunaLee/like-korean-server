# Generated by Django 3.2.16 on 2024-01-11 13:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import like_korean.apps.users.models.fields.phone_number
import like_korean.apps.users.models.managers.active
import like_korean.apps.users.models.managers.objects
import like_korean.apps.users.models.mixins.image
import like_korean.bases.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('languages', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=like_korean.apps.users.models.mixins.image.image_path, verbose_name='프로필 이미지')),
                ('profile_image_url', models.URLField(blank=True, null=True, verbose_name='프로필 이미지 URL')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='이메일')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='닉네임')),
                ('phone', like_korean.apps.users.models.fields.phone_number.CustomPhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='전화')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='languages.language')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'users',
                'ordering': ['-created'],
            },
            bases=(like_korean.bases.models.UpdateMixin, models.Model),
            managers=[
                ('objects', like_korean.apps.users.models.managers.objects.UserMainManager()),
                ('active', like_korean.apps.users.models.managers.active.UserActiveManager()),
            ],
        ),
    ]