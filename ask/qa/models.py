from django.db import models
from django.contrib.auth.models import User




class QuestionManager(models.Manager):
    def new(self):
        return self.ordered('-id')

    def popular(self, x='rating'):
        return self.ordered('-' + x)

    def answer_set(self):
        return Answer.objects.filter(question=self)

    def all(self):
        return self.all()

    def aggregate(self):
        return self

    def Max(self, x='rating'):
        return self.popular(self, x)


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')
    objects = QuestionManager()

    def get_url(self):
        url = '/question/' + str(self.id) + '/'
        return url


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

