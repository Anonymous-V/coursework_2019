from django.contrib import admin
from .models import Comments

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created', 'message', 'active',)
    list_filter = ('active', 'created',)

admin.site.register(Comments, CommentAdmin)