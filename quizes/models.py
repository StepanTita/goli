from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# TODO rename to Quiz
class Vote(models.Model):
    title = models.TextField(blank=False, null=False)
    quiz_type = models.TextField(blank=False, null=False)
    timestamp = models.PositiveBigIntegerField(blank=False, null=False)
    goal = models.PositiveBigIntegerField(blank=False, null=False)
    indicator_value = models.FloatField(blank=False, null=False)
    vote_detail = models.JSONField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    description = models.TextField(blank=False, null=False, default='This is a default quiz')

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


@receiver(pre_save, sender=VoteChoice)
def calculate_indicator(sender, instance, *args, **kwargs):
    voters = VoteChoice.objects.filter(quiz=instance.quiz).distinct('user')
    instance.quiz.indicator_value = min(1, len(voters) / instance.quiz.goal)
    instance.quiz.save()
