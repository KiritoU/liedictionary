from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Word(models.Model):
    word = models.CharField(max_length=255, help_text="Word")
    description = models.TextField(help_text="Description")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('dictionary:word-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('word',)