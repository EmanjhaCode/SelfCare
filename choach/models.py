from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=300)
    image=models.FileField(upload_to='blog',default="")
    paragraph1=models.CharField(max_length=2000, default="empty")
    paragraph2=models.CharField(max_length=2000, default="empty")
    paragraph3=models.CharField(max_length=2000, default="empty")


class Services(models.Model):
    title=models.CharField(max_length=300)
    image=models.FileField(upload_to='service',default="")
    paragraph1=models.CharField(max_length=2000, default="empty")
    paragraph2=models.CharField(max_length=2000, default="empty")
    paragraph3=models.CharField(max_length=2000, default="empty")

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100, default="empty")
    no=models.CharField(max_length=20, default="empty")
    msg=models.CharField(max_length=2000, default="empty")


class Subscribe(models.Model):
    em=models.CharField(max_length=100)


# Create your models here.
class Programs(models.Model):
    title=models.CharField(max_length=300)
    image=models.FileField(upload_to='blog',default="")
    paragraph1=models.CharField(max_length=2000, default="empty")
    paragraph2=models.CharField(max_length=2000, default="empty")
    paragraph3=models.CharField(max_length=2000, default="empty")


class Products(models.Model):
    title=models.CharField(max_length=300)
    image=models.FileField(upload_to='service',default="")
    paragraph1=models.CharField(max_length=2000, default="empty")
    paragraph2=models.CharField(max_length=2000, default="empty")
    paragraph3=models.CharField(max_length=2000, default="empty")
