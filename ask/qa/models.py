from django.db import models
from django.contrib.auth import models as auth_models


class QuestionManager(models.Model):
    def new(self):
        return self.ordering('-added_at')

    def popular(self):
        return self.ordering('-rating')


class QaUser(auth_models.User):
    pass


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = QaUser()
    likes = models.ManyToManyField(QaUser)


class Answer(models.Model):
    text = models.TextField
    added_at = models.DateTimeField(auto_now_add=True)
    question = Question()
    author = QaUser()
