from rest_framework import response, status
from rest_framework import permissions
from rest_framework import views

from users import serializers

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreateUserAPIView(views.APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (permissions.AllowAny,)

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
                coreapi.Field(
                    name="groups",
                    required=True,
                    location='form',
                    schema=coreschema.Integer(
                        title="Group of a user",
                        description="user group id",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request):
        user = request.data
        serializer = serializers.UserSerializer(data=user)
        if not serializer.is_valid(raise_exception=False):
            logger.error("user serializer error")
        serializer.save()
        return response.Response({"user": serializer.data, "status": status.HTTP_200_OK})
