from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserQuestion


@login_required
def add_question(request):
    if request.method == 'POST':
        form = UserQuestion(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()

            url_question = reverse('single_post',
                                   args=(new_question.language.slug, new_question.id,))
            text = _('Вопрос <a href="{0}">{1}</a> был успешно добавлен')\
                .format(url_question, new_question.title)
            messages.add_message(request, messages.SUCCESS, text)

            return redirect(reverse('question'))
    else:
        form = UserQuestion()
    return render(request, 'question/add_question.html', {'form': form})