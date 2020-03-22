from django.shortcuts import render
from question.models import Question


def get_index_page(request):
    posts = Question.objects.all()[:4]

    return render(request, 'index/lists.html', {'posts': posts})
