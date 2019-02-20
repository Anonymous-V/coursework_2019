from django.contrib import admin
from .models import Comments

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created', 'message', 'active',)
    list_filter = ('active', 'created',)