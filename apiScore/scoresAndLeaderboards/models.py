from django.db import models
import uuid
# Create your models here.

class Score(models.Model):
    username = models.CharField(max_length=200, unique=True)
    gameID = models.CharField(max_length=200)
    scoreValue = models.IntegerField()
    scoreUUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)
    timeRecorded = models.DateTimeField(auto_now_add=True)


