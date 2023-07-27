from django.db import models

class list(models.Model):
    rating = models.IntegerField(max_length=200)
    nickname = models.TextField(max_length=200, unique = True)
    avatar = models.ImageField(upload_to ="C:/Users/Stud1/Documents/Sekrier/djangotest/myproj/myapp/static/img" )
    specialization = models.TextField(max_length=2000, verbose_name = True)
    experience = models.TextField(max_length=2000)
    service = models.TextField(max_length=2000)
    price = models.TextField(max_length=100)




class buy_tech(models.Model):
    id_user = models.IntegerField()
    id_tech = models.IntegerField()

class price_list(models.Model):
    name = models.CharField(max_length=300)
    specialization = models.CharField(max_length=500)
    service = models.CharField(max_length=5000)
    cost = models.CharField(max_length=1000)