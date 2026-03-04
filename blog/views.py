from django.utils import timezone
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).select_related("author")

