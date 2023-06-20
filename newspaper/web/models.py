from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.UUIDField()
    title = models.TextField()
    author = models.TextField()
    date_published = models.DateTimeField()
    #image = models.ImageField(null=True)
    textual_content = models.TextField()
