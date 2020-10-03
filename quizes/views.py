from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from quizes import models, serializers

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema


class QuizAPIView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="title",
                    required=False,
                    location='form',
                    schema=coreschema.String(
                        title="Title",
                        description="name of a quiz",
                    ),
                ),
                coreapi.Field(
                    name="quiz_type",
                    required=False,
                    location='form',
                    schema=coreschema.String(
                        title="Type of a quiz",
                        description="Type of a quiz",
                    ),
                ),
                coreapi.Field(
                    name="timestamp",
                    required=False,
                    location='form',
                    schema=coreschema.Integer(
                        title="Timestamp",
                        description="timestamp",
                    ),
                ),
                coreapi.Field(
                    name="goal",
                    required=False,
                    location='form',
                    schema=coreschema.Integer(
                        title="Goal",
                        description="goal for the users",
                    ),
                ),
                coreapi.Field(
                    name="indicator_value",
                    required=False,
                    location='form',
                    schema=coreschema.Number(
                        title="Indicator value",
                        description="indicator value",
                    ),
                ),
                coreapi.Field(
                    name="vote_detail",
                    required=False,
                    location='form',
                    schema=coreschema.Object(
                        title="Vote detail",
                        description="vote details in json format",
                    ),
                ),
            ],
            encoding="application/json",
        )
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.QuizSerializer
    queryset = models.Vote.objects.all()


class QuizListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.QuizSerializer
    queryset = models.Vote.objects.all()


class VoteAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.VoteChoiseSerializer