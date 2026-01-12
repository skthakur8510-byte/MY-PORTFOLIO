from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Skills(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class Profile(models.Model):
    name=models.CharField(max_length=20)
    about=HTMLField()
    photo=models.ImageField(upload_to='profile/')
    skill=models.ManyToManyField(Skills)
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.name
