from django.db import models

# Create your models here.
class chat(models.Model):
    tag = models.CharField(max_length=400)
    patterns = models.CharField(max_length=5000)
    responses = models.CharField(max_length=5000)

class bot_user(models.Model):
    user_id = models.CharField(max_length=80)
    user_res = models.CharField(max_length=50000)
    bot_res = models.CharField(max_length=50000)
