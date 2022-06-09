from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from markdown import markdown
from markdownx.models import MarkdownxField


class Diary(models.Model):
    title = models.CharField(max_length=30)
    content= MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/diaries/{self.pk}'

    def get_content_markdown(self):
        return markdown(self.content)