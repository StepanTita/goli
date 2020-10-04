from django.db.models import Count

# Create your views here.
from rest_framework import generics, permissions, views, response, authentication, status

from quizes import models, serializers

from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.pagination import PageNumberPagination


class PageNumberSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'


class CreateQuizAPIView(generics.CreateAPIView):
    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="title",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Title",
                        description="name of a quiz",
                    ),
                ),
                coreapi.Field(
                    name="quiz_type",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Type of a quiz",
                        description="Type of a quiz",
                    ),
                ),
                coreapi.Field(
                    name="timestamp",
                    required=True,
                    location='form',
                    schema=coreschema.Integer(
                        title="Timestamp",
                        description="timestamp",
                    ),
                ),
                coreapi.Field(
                    name="goal",
                    required=True,
                    location='form',
                    schema=coreschema.Integer(
                        title="Goal",
                        description="goal for the users",
                    ),
                ),
                coreapi.Field(
                    name="indicator_value",
                    required=True,
                    location='form',
                    schema=coreschema.Number(
                        title="Indicator value",
                        description="indicator value",
                    ),
                ),
                coreapi.Field(
                    name="vote_detail",
                    required=True,
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


class QuizAPIView(generics.RetrieveUpdateDestroyAPIView):
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
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.QuizSerializer
    queryset = models.Vote.objects.all()
    pagination_class = PageNumberSetPagination


# TODO check quizes are only created by staff
class VoteAPIView(generics.CreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.VoteChoiseSerializer


class ListCountVoteAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, **kwargs):
        quiz_id = kwargs.get('pk', -1)
        if quiz_id == -1:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        votes = models.VoteChoice.objects.filter(quiz_id=quiz_id).values('choice').annotate(Count('user'))
        return response.Response(votes, status=status.HTTP_200_OK)


class ListVoteAPIView(generics.ListAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.VoteChoiseSerializer
    queryset = models.VoteChoice.objects.all()
