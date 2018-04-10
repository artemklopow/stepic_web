from django.db import models
from django.contrib.auth import models as auth_models


class QuestionManager(models.Model):
    def new(self):
        return self.ordering('-added_at')

    def popular(self):
        return self.ordering('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    likes = models.ManyToManyField(auth_models.User, related_name='question_like_user')


class Answer(models.Model):
    text = models.TextField
    added_at = models.DateField(auto_now_add=True)
    question = models.OneToOneField(Question, null=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
