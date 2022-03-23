from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=3000)
    source = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    publishedDate = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    photoUrl = models.CharField(max_length=500)
    readTime = models.CharField(max_length=300)
