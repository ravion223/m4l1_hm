from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length = 63)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    post_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, default = None, related_name = "posts")

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return timezone.now() - timedelta(days = 7) < self.published_date
    
class Commentary(models.Model):
    author_name = models.CharField(max_length = 63)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(Post, on_delete = models.DO_NOTHING, default = None, related_name = "commentaries")

    def __str__(self):
        return self.author_name