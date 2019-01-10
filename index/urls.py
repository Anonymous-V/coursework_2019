from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index_page, name='index_page'),
]