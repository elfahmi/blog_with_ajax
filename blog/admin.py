from django.contrib import admin

from .models import Page, Comment


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'page']
