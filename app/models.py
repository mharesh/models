from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=150,primary_key=True)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    url=models.URLField()
 
class Access_Record(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    detail=models.CharField(max_length=130)