from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Model):
    def new(self):
        return self.ordering('-added_at')

    def popular(self):
        return self.ordering('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField(null=False)
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=False, on_delete=models.SET('Пользователь удален'))
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField(null=False)
    added_at = models.DateField(auto_now_add=True)
    question = models.OneToOneField(Question, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.SET('Пользователь удален'))
