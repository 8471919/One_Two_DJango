from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/diaries/{self.pk}'