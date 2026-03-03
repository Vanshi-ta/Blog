from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).select_related("author")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"