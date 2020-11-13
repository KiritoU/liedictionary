from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Word


class WordListView(ListView):
    model = Word
    context_object_name = 'words'
    template_name = 'dictionary/home.html'
    paginate_by = 4

    def get_queryset(self):
        letter = self.request.GET.get('q')
        if letter:
            return Word.objects.filter(word__istartswith = letter)
        return Word.objects.all()

class LetterListView(ListView):
    model = Word
    context_object_name = 'words'
    template_name = 'dictionary/home.html'
    paginate_by = 4

    def get_queryset(self):
        return Word.objects.filter(word__istartswith=self.request.GET.get('q'))

class WordDetailView(DetailView):
    model = Word

class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    fields = [
        'word',
        'description',
        'video',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    fields = [
        'word',
        'description',
        'video',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Word
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False