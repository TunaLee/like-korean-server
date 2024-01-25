# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Django Rest Framework
from rest_framework.authtoken.models import Token



# Local
from like_korean.apps.users.api.serializers import UserSerializer
from like_korean.apps.users.models import User


# 유저 객체 생성, 수정 후 동작하는 로직
@receiver(post_save, sender=User)
def user_token_post_save(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

    profile_image = instance.profile_image
    user = User.objects.filter(id=instance.pk)

    # 프로필 이미지 생성, 수정시, 프로필 절대 경로 URL 저장
    if profile_image:
        user.update(profile_image_url=instance.profile_image.url)

    # 유저 수정시, 클럽 업데이트
    instance.clubs.update(user_data=UserSerializer(instance=instance).data)

    # 유저 수정시, 클럽 프로필 업데이트
    instance.profiles.update(user_data=UserSerializer(instance=instance).data)
