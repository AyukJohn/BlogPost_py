from django.db import models

# Create your models here.


class AboutMe(models.Model):
    aboutMe = models.TextField(max_length=8050)
    aboutBlog = models.TextField(max_length=8050)
    mySkills = models.TextField(max_length=8050)
    myProjects = models.TextField(max_length=8050)
    img = models.ImageField(upload_to = "images/%y", blank=False, null=False)

    def __str__(self):
        return self.aboutMe
