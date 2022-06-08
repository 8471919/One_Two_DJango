from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

