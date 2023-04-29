from django.contrib import admin
from todo.models import TodoItem


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

# Register your models here.
admin.site.register(TodoItem)