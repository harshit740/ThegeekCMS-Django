from django.shortcuts import render
from django.views import generic
from blog.models import Post ,Category


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/postlist.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostListbycategory(generic.ListView):
    template_name = 'blog/postlist.html'
    model = Post

    def get_queryset(self):
        print(self.kwargs.get('slug', None) )
        return Post.objects.filter(category__slug=self.kwargs.get('slug', None) ).order_by('-publish_on')
