from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Answer, QuestionManager, Question
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_details(request, question_id):
    try:
        que = Question.objects.get(question_id=question_id)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.objects.filter(question=que)
    except Answer.DoesNotExist:
        answers = None

    return render(request, 'question_details.html', {
        'que': que,
        'answers': answers
    })


def question_popular(request, page=1):
    try:
        que = Question.objects.all.popular()
    except Question.DoesNotExist:
        raise Http404
    try:
        page = int(page)
    except ValueError:
        page = 1
    paginator = Paginator(que, 10)
    page = paginator.page(page)
    return render(request, 'question_popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


def question_new(request, page=1):
    try:
        que = Question.objects.all.new()
    except Question.DoesNotExist:
        raise Http404
    try:
        page = int(page)
    except ValueError:
        page = 1
    paginator = Paginator(que, 10)
    page = paginator.page(page)
    return render(request, 'question_new.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

