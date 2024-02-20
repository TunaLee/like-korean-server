# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from like_korean.apps.users.api.serializers import UserSignUpSerializer, UserSignInSerializer, \
    UserSerializer, UserMeSerializer, UserValidateEmailSerializer
from like_korean.apps.users.decorators import signup_decorator, signin_decorator, validate_email_decorator, me_decorator

# Models
from like_korean.apps.users.models import User
from like_korean.bases.api import mixins

# Bases
from like_korean.bases.api.viewsets import GenericViewSet

# Utils
from like_korean.utils.api.response import Response
from like_korean.utils.decorators import retrieve_decorator, list_decorator


# Class Section
class UserViewSet(GenericViewSet,
                  mixins.RetrieveModelMixin):
    queryset = User.active.all()
    filter_backends = (DjangoFilterBackend,)

    serializers = {
        'default': UserSerializer,
        'validate_email': UserValidateEmailSerializer,
        'me': UserMeSerializer,
        'signup': UserSignUpSerializer,
        'signin': UserSignInSerializer
    }

    @swagger_auto_schema(**list_decorator(title=_('유저'), serializer=UserSerializer))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-correct_solved')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            message=_('ok'),
            status=status.HTTP_200_OK,
            code=200,
            data=serializer.data
        )

    @swagger_auto_schema(**validate_email_decorator(title=_('유저')))
    @action(detail=False, methods=['get'])
    def validate_email(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not User.objects.filter(email=email).exists():
            return Response(
                message=_('validate email'),
                status=status.HTTP_200_OK,
                code=200
            )
        else:
            return Response(
                message=_('duplicate email address'),
                status=status.HTTP_400_BAD_REQUEST,
                code=400
            )

    @swagger_auto_schema(**me_decorator(title=_('유저'), serializer=UserMeSerializer))
    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=UserMeSerializer(instance=request.user).data
        )

    @swagger_auto_schema(**signup_decorator(title=_('유저'), request_body=UserSignUpSerializer))
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            nationality = serializer.validated_data['nationality']
            User.objects.create_user(username=username, email=email, password=password, nationality=nationality)
            return Response(
                message=_('Signup success.'),
                code=201,
                status=status.HTTP_201_CREATED
            )

    @swagger_auto_schema(**signin_decorator(title=_('유저'), request_body=UserSignInSerializer))
    @action(detail=False, methods=['post'])
    def signin(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.get(email=email)
            if not user.check_password(password):
                return Response(
                    message=_('Password incorrect.'),
                    code=400,
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token = Token.objects.get(user=user)
            return Response(
                message=_('Token created.'),
                code=201,
                status=status.HTTP_201_CREATED,
                data={'token': token.key}
            )
