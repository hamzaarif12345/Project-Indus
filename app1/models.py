from django.db import models

# Create your models here.
# models.py

from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class MyModel2(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()

class MyModel3(models.Model):
    phone_number = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    type_your_message = models.TextField()
