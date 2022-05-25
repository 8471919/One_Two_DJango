from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    