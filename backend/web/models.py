from django.db import models


class User(models.Model):
    email = models.EmailField(primary_key=True)
    is_subscribed = models.BigIntegerField(default=0)

    def is_subscribed_to_channel(self, channel):
        return self.is_subscribed & channel != 0


# Create your models here.
class Article(models.Model):
    article_id = models.UUIDField()
    title = models.TextField()
    author = models.TextField()
    date_published = models.DateTimeField()
    # image = models.ImageField(null=True)
    textual_content = models.TextField()
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.article_id)
