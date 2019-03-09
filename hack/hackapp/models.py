from django.db import models
class Request(models.Model):
    req_blood_group = models.CharField(max_length=20)
    req_city = models.CharField(max_length=30)
    req_add = models.CharField(max_length=300)

class Donor(models.Model):
    don_blood_group = models.CharField(max_length=20)
    don_city = models.CharField(max_length=30)
    don_mail = models.CharField(max_length=30)
    don_contact = models.CharField(max_length=30)
    don_add = models.CharField(max_length=300)


from django.contrib.auth.models import User
class details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    add = models.CharField(max_length=300)


# Create your models here.
