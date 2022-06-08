from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from main_diary.models import Diary


class DiaryList(LoginRequiredMixin, ListView):
    model = Diary
    ordering = '-created_at'

    def get_queryset(self):
        qs = super().get_queryset()
        if (self.request.user):
            qs = qs.filter(author=self.request.user.id)
            return qs
        else:
            return redirect('/')


class DiaryDetail(LoginRequiredMixin, DetailView):
    model = Diary


