from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Order(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30)
    instructions = models.TextField(max_length=200, null=True, verbose_name="Write your instructions Here")
    urgency = models.IntegerField(choices=list(zip(range(1, 10), range(0, 10))))
    pages = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    email = models.EmailField(null=True)


    def __str__(self):

        return str(self.user)

