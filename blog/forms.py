from django import forms
from blog.models import Comment, Article


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'title',
            'author',
            'body',
            'status'
        ]