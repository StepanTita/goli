from django.contrib import admin

# Register your models here.
from quizes import models

admin.register(models.Vote)
admin.register(models.VoteChoice)
