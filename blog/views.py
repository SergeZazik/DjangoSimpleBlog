from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Article
from .forms import CommentForm, ArticleModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(status='published')


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# def post_detail(request, pk):
#     post = get_object_or_404(Article, pk=pk)
#     comments = post.comments.filter(active=True)
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#
#         if comment_form.is_valid():
#             try:
#                 parent_id = request.POST['comment_id']
#             except:
#                 parent_id = None
#
#             comment = comment_form.save(commit=False)
#             comment.post = post
#
#             if not parent_id is None:
#                 comment.parent = comments.get(id=parent_id)
#             comment.save()
#             return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'articles/article_detail.html',
#                   {'post': post,
#                    'comments': comments,
#                    'comment_form': comment_form})