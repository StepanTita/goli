import json
import logging

# Get an instance of a logger
from django.contrib.auth import models
from rest_framework import permissions, views, response, status

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

from users import serializers

logger = logging.getLogger(__name__)


# TODO add permissions to authenticated
class CreateGroupAPIView(views.APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (permissions.AllowAny,)

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="users",
                    required=False,
                    location='form',
                    schema=coreschema.Array(
                        items={"email": "string"},
                        title="Email",
                        description="an array with users of a group",
                    ),
                ),
                coreapi.Field(
                    name="group",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Groupt name",
                        description="a string with a group name",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request):
        group = request.data
        serializer = serializers.GroupSerializer(data=group)
        if not serializer.is_valid(raise_exception=False):
            logger.error("group serializer error")
        serializer.save()
        return response.Response({"group": serializer.data, "status": status.HTTP_200_OK})


class GetUserAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, user_id):
        user = models.User.objects.get(id=user_id)
        serializer = serializers.UserSerializer(user)
        if not serializer.is_valid(raise_exception=False):
            logger.error("user serializer error")
        serializer.save()
        return response.Response({"group": serializer.data, "status": status.HTTP_200_OK})


class AddGroupUsersAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="users",
                    required=False,
                    location='form',
                    schema=coreschema.Array(
                        items={"email": "string"},
                        title="Email",
                        description="an array with users of a group",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def patch(self, request, group_name):
        group = models.Group.objects.get(name=group_name)
        users_emails = json.loads(request.data)
        for user_email in users_emails:
            user = models.User.objects.get(email=user_email)
            group.user_set.add(user)
        return response.Response({"status": status.HTTP_204_NO_CONTENT})