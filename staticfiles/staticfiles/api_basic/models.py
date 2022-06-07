from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length= 255)
    subtitle = models.TextField(max_length= 855)
    body = models.TextField(max_length=8050)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to = "images/%y", blank=False, null=False)

    class Meta:
        ordering = ['date']


class Comment(models.Model):
    comments = models.CharField(max_length=200)
    emailAddress = models.EmailField(max_length= 255, null=False)
    article = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)