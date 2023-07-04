from django.db import models


class U(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    is_subscribed = models.BooleanField()
    
# Create your models here.
class Article(models.Model):
    article_id = models.UUIDField()
    title = models.TextField()
    author = models.TextField()
    date_published = models.DateTimeField()
    #image = models.ImageField(null=True)
    textual_content = models.TextField()
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.article_id)