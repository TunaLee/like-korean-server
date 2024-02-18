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

def signup_decorator(title='', request_body=None):
    return dict(
        operation_id=_('회원 가입'),
        operation_description=_(
            '## < 회원가입 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )
