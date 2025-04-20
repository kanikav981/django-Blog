from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title=models.TextField(max_length=50)
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    content=models.CharField(max_length=8000)
    graphics=models.ImageField(upload_to="photos/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author.username[:10]}'
