from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    post_image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def __str__(self):
        return self.title