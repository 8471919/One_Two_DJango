from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
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

class DiaryCreate(LoginRequiredMixin, CreateView):
    model = Diary
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(DiaryCreate, self).form_valid(form)
        else:
            return redirect('/')

class DiaryUpdate(LoginRequiredMixin, UpdateView):
    model = Diary
    fields = ['title', 'content', 'image']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(DiaryUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return PermissionDenied

class DiaryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diary
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and request.user == self.get_object().author:
    #         return super(DiaryUpdate, self).dispatch(request, *args, **kwargs)
    #     else:
    #         return PermissionDenied

