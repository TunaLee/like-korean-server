# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def me_decorator(title='', serializer=None):
    return dict(
        operation_id=_('내 정보'),
        operation_description=_(
            '## < 내 정보 조회 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')]
    )
