from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from CMS import settings
from blog.models import Post, PostImage
from user.forms import NewBlog


# Create your views here.


def userpostlist(request):
    ispub = {'pub': 'Published', 'unpub': 'Drafts'}
    postobjects = Post.objects.filter(author=request.user)
    return render(request, 'user/user_postlist.html', {'posts': postobjects, 'pub': ispub})

def newpost(request):
    if request.method == 'POST':
        newblogfrom = NewBlog(request.POST, request.FILES)
        if newblogfrom.is_valid():
            newblogobject = newblogfrom.save(commit=False)
            newblogobject.author = request.user
            newblogobject.save()
            return redirect('home')
        else:
            print(newblogfrom.errors)
            return render(request, 'user/newPost.html', {'form': newblogfrom})
    else:
        newblogfrom = NewBlog()

        return render(request, 'user/newPost.html', {'form': newblogfrom, })

def ImageUploader(request):
    print(request.FILES)
    if request.method == 'POST':
        data = {
            'image': request.FILES['image'],
            'auhor': request.user
        }
        image = PostImage.objects.create(**data)
        url = '/' + settings.MEDIA_ROOT + str(image.image)
        print(url)
        return JsonResponse({'location': url, 'message': 'success'})
    else:
        return redirect('/new')

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('userpostlist')
    template_name = 'user/post_delete.html'

    def get_obj(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostDelete, self).get_object()
        print(obj.author)
        if not obj.author == self.request.user or not self.request.user.is_superuser:
            raise Http404
        return obj

class PostEdit(generic.UpdateView):
    model = Post
    form_class = NewBlog
    success_url = reverse_lazy('userpostlist')
    template_name = 'user/newPost.html'

    def get_obj(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostEdit, self).get_object()
        print(obj.author)
        if not obj.author == self.request.user or not self.request.user.is_superuser:
            raise Http404
        return obj



