from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    authour = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.title
