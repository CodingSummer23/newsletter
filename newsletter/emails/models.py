from django.db import models
from datetime import datetime


class Subscription(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    date_added = models.DateTimeField(default=datetime.now())
    unsubscribe_hash = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email
