from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)