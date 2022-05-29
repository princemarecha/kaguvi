from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):

    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name="customer")
    name = models.CharField(max_length=255, unique=False)
    car = models.CharField(max_length=255, default="")
    model = models.CharField(max_length=255, default="")
    engine = models.CharField(max_length=255, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

