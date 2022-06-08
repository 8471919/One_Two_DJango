from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class DiaryCreate(CreateView):
    model = Diary
    fields = ['title', 'content', 'image']


class DiaryUpdate(UpdateView):
    model = Diary

class DiaryDelete(DeleteView):
    model = Diary

