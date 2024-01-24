# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def create_decorator(title=''):
    return dict(
        operation_id=_('생성'),
        operation_description=_(
            '## < 객체 생성 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def token_create_decorator(title=''):
    return dict(
        operation_id=_('생성'),
        operation_description=_(
            '## < 객체 생성 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('리스트 조회'),
        operation_description=_(
            '## < 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def token_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('리스트 조회'),
        operation_description=_(
            '## < 리스트 조회 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def retrieve_decorator(title='', serializer=None):
    return dict(
        operation_id=_('객체 조회'),
        operation_description=_(
            '## < 객체 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def token_retrieve_decorator(title='', serializer=None):
    return dict(
        operation_id=_('객체 조회'),
        operation_description=_(
            '## < 객체 조회 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def patch_decorator(title=''):
    return dict(
        operation_id=_('수정'),
        operation_description=_(
            '## < 객체 수정 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. `id` 입력 \n'
            '### 4. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def token_patch_decorator(title=''):
    return dict(
        operation_id=_('수정'),
        operation_description=_(
            '## < 객체 수정 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. `id` 입력 \n'
            '### 4. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def destroy_decorator(title=''):
    return dict(
        operation_id=_('삭제'),
        operation_description=_(
            '## < 객체 삭제 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute'
        ),
        responses={204: openapi.Response(_('no content'))},
        tags=[_(f'{title}')]
    )


def token_destroy_decorator(title=''):
    return dict(
        operation_id=_('삭제'),
        operation_description=_(
            '## < 객체 삭제 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute'
        ),
        responses={204: openapi.Response(_('no content'))},
        tags=[_(f'{title}')]
    )

