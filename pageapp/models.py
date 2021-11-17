from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=40)
    publish_date = models.DateTimeField()


