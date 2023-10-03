from django.db import models
# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)

class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    url=models.URLField()

