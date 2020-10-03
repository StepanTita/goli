from django.contrib.auth.models import User
from django.db import models


# TODO rename to Quize
class Vote(models.Model):
    title = models.TextField(blank=False, null=False)
    quiz_type = models.TextField(blank=False, null=False)
    timestamp = models.PositiveBigIntegerField(blank=False, null=False)
    goal = models.PositiveBigIntegerField(blank=False, null=False)
    indicator_value = models.FloatField(blank=False, null=False)
    vote_detail = models.JSONField()

    def __str__(self):
        return self.title


# TODO rename to Vote
class VoteChoice(models.Model):
    quiz = models.ForeignKey(Vote, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")
    choice = models.PositiveBigIntegerField(blank=False, null=False)

    class Meta:
        unique_together = ('quiz', 'user', 'choice',)

    def __str__(self):
        return f"{self.quiz}:{self.user}"
