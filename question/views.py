from django.shortcuts import render
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
            return render(request, 'question/add_question_success.html')
    else:
        form = UserQuestion()
    return render(request, 'question/add_question.html', {'form': form})