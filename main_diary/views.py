from django.views.generic import ListView

from main_diary.models import Diary


class DiaryList(ListView):
    model = Diary