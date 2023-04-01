from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings

class Workout(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.title