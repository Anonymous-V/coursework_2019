from django.contrib import admin
from .models import Question, AvailableLanguage

class PostQuestions(admin.ModelAdmin):
    list_display = ('title', 'language', 'author', 'date', 'audio',)
    list_filter = ('language', 'author', 'date',)

class PostAvailableQuestions(admin.ModelAdmin):
    list_display = ('lang', 'image', 'slug', 'lang_code',)
    prepopulated_fields = {'lang_code': ('lang',)}

admin.site.register(Question, PostQuestions)
admin.site.register(AvailableLanguage, PostAvailableQuestions)