from django.contrib.auth import models
from rest_framework import permissions
from rest_framework import generics

from users import serializers

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreateUserAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (permissions.AllowAny,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="user login",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
                coreapi.Field(
                    name="first_name",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="First name",
                        description="user first name",
                    ),
                ),
                coreapi.Field(
                    name="last_name",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Last name",
                        description="user last name",
                    ),
                ),
                coreapi.Field(
                    name="is_staff",
                    required=True,
                    location='form',
                    schema=coreschema.Boolean(
                        title="User status",
                        description="is user staff",
                    ),
                ),
            ],
            encoding="application/json",
        )
