from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})


class Comment(MPTTModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return 'Comment by {}'.format(self.author)
