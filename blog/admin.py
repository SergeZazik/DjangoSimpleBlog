from django.contrib import admin
from .models import Comment, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)