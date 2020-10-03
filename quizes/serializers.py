from rest_framework import serializers

import logging

# Get an instance of a logger
from quizes.models import Vote

logger = logging.getLogger(__name__)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'title', 'quiz_type', 'timestamp', 'goal', 'indicator_value', 'vote_detail']
