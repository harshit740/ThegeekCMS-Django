from django.views import generic
from blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/postlist.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

