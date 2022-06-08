from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from main_diary.models import Diary


class DiaryList(LoginRequiredMixin, ListView):
    model = Diary
    ordering = '-created_at'

class DiaryDetail(LoginRequiredMixin, DetailView):
    model = Diary