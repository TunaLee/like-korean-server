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
    UserSerializer
from like_korean.apps.users.decorators import signup_decorator, signin_decorator, validate_email_decorator

# Models
from like_korean.apps.users.models import User
from like_korean.bases.api import mixins

# Bases
from like_korean.bases.api.viewsets import GenericViewSet

# Utils
from like_korean.utils.api.response import Response
from like_korean.utils.decorators import retrieve_decorator


# Class Section
class UserViewSet(GenericViewSet,
                  mixins.RetrieveModelMixin):
    queryset = User.active.all()
    filter_backends = (DjangoFilterBackend,)

    serializers = {
        'default': UserSerializer,
        'signup': UserSignUpSerializer,
        'signin': UserSignInSerializer
    }
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

