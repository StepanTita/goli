import json
import logging

# Get an instance of a logger
from rest_framework import generics
from django.contrib.auth import models
from rest_framework import permissions, views, response, status

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema

from users import serializers

logger = logging.getLogger(__name__)


# TODO add permissions to authenticated
class GroupAPIView(generics.RetrieveUpdateDestroyAPIView):

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
                        title="Group name",
                        description="a string with a group name",
                    ),
                ),
            ],
            encoding="application/json",
        )

    # Allow any user (authenticated or not) to access this url
    permission_classes = (permissions.AllowAny,)
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    lookup_field = 'name'


class UserAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    lookup_field = 'username'


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

    def patch(self, request, **kwargs):
        group_name = kwargs.get('group_name', 'default')
        try:
            group = models.Group.objects.get(name=group_name)
        except models.Group.DoesNotExist:
            logger.info(f"group={group_name} - group not found")
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        users_emails = json.loads(request.data)
        for user_data in users_emails:
            if "email" not in user_data:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)
            user = models.User.objects.get(email=user_data['email'])
            group.user_set.add(user)
        return response.Response({"group": group, status: status.HTTP_200_OK})


