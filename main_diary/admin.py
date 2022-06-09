from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Diary

# Register your models here.
admin.site.register(Diary, MarkdownxModelAdmin)