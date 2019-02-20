from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from question.models import Question, AvailableLanguage
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comments
import datetime


def blog(request, posts, pages):
    obj = dict()

    paginator = Paginator(posts, pages)
    page = request.GET.get('page', 1)

    obj['single_header_post'] = posts.first()
    obj['posts'] = paginator.get_page(page)
    obj['page_count'] = paginator.num_pages

    return obj

def all_posts(request):
    posts = Question.objects.all()
    posts_all = blog(request, posts, 6)

    return render(request, 'blog/all_posts.html', posts_all)

def lang_posts(request, lang_slug):
    lang = AvailableLanguage.objects.get(slug=lang_slug)
    posts = Question.objects.all().filter(language_id=lang.id)

    all_objects = blog(request, posts, 6)
    all_objects['post_img'] = lang.image

    return render(request, 'blog/all_posts.html', all_objects)


def date_posts(request, year, month, day):
    date = datetime.date(year, month, day)
    posts = Question.objects.all().filter(date=date)

    return render(request, 'blog/all_posts.html', blog(request, posts, 6))

@login_required
def single_post(request, lang_slug, post_id):

    lang = AvailableLanguage.objects.get(slug=lang_slug)
    post = Question.objects.get(id=post_id)
    post_pred = Question.objects.filter(language_id=lang.id,
                                        id__lt=post_id).first()
    post_next = Question.objects.filter(language_id=lang.id,
                                        id__gt=post_id).last()
    comments = Comments.objects.filter(post=post_id, active=True)

    all_comments = blog(request, comments, 5)
    print(all_comments)
    all_comments['post'] = post
    all_comments['post_pred'] = post_pred
    all_comments['post_next'] = post_next
    all_comments['post_img'] = lang.image

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, files=request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()

            messages.add_message(request, messages.SUCCESS,
                                 _('Ваш комментарий был успешно добавлен'))

            all_comments['comment_form'] = comment_form

            return redirect(request.path)
        else:
            return render(request, 'blog/single_question.html', all_comments)
    else:
        comment_form = CommentForm()
        all_comments['comment_form'] = comment_form

    return render(request, 'blog/single_question.html', all_comments)