from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.published.get_queryset()


class ArticleCreate(CreateView):
    model = Post
    template_name = 'blog/create.html'
    success_url = reverse_lazy('home')
    fields = ['title', 'author', 'body', 'status']


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            try:
                parent_id = request.POST['comment_id']
            except:
                parent_id = None

            comment = comment_form.save(commit=False)
            comment.post = post

            if not parent_id is None:
                comment.parent = comments.get(id=parent_id)
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})