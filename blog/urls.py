from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:year>-<int:month>-<int:day>', views.date_posts, name='date_posts'),
    path('<slug:lang_slug>/<int:post_id>', views.single_post, name='single_post'),
    path('<slug:lang_slug>/<int:post_id>/add_rating', views.single_post_rating, name='single_post_rating'),
    path('<slug:lang_slug>', views.lang_posts, name='lang_posts'),
]
