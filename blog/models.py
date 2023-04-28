from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length = 10000, default=None)
    uploadTime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title