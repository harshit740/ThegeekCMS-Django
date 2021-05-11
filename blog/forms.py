from django.forms import ModelForm
from blog.models import PostImage, Post


class ImageFileUploadForm(ModelForm):
    class Meta:
        model = PostImage
        fields = ('image', 'author')


class NewBlog(ModelForm):
    class Meta:
        model = Post
