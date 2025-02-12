import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now, timedelta

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_permissions_set', blank=True
    )

    reset_token = models.CharField(max_length=100, blank=True, null=True, unique=True)
    reset_token_expires_at = models.DateTimeField(blank=True, null=True)

    def generate_reset_token(self):
        self.reset_token= str(uuid.uuid4())
        self.reset_token_expires_at = now() + timedelta(minutes=10)
        self.save()