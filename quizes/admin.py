from django.contrib import admin

# Register your models here.
from quizes import models

admin.site.register(models.Vote)
admin.site.register(models.VoteChoice)
