from django.db import models


class Post(models.Model):
    title     = models.CharField(max_length=120)
    content   = models.TextField(max_length=500)
    updated   = models.DateTimeField(auto_now=True, auto_now_add= False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

# Create your models here.
