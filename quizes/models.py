from django.db import models


# Create your models here.
class Vote(models.Model):
    title = models.TextField(blank=False, null=False)
    quiz_type = models.TextField(blank=False, null=False)
    timestamp = models.PositiveBigIntegerField(blank=False, null=False)
    goal = models.PositiveBigIntegerField(blank=False, null=False)
    indicator_value = models.FloatField(blank=False, null=False)
    vote_detail = models.JSONField()

    def __str__(self):
        return self.title
