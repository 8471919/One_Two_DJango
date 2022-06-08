from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from main_diary.models import Diary


class DiaryList(LoginRequiredMixin, ListView):
    model = Diary
