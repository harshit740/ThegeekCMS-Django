from django.forms import ModelForm, forms
from blog.models import PostImage, Post
from django import forms

class NewBlog(ModelForm):
    title = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter Title For the Bog'}))
    byline = forms.CharField(max_length=400, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter byline'}))
    content = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder': 'Enter Content'}))
    class Meta:
        model = Post
        exclude = ('slug','is_published','updated_on','created_on','publish_on','author','list_display','search_fields','list_filter','date_hierarchy')

    def __init__(self, *args, **kwargs):
        super(NewBlog, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'input is-medium'
        self.fields['featured_image'].widget.attrs['id'] ="file"
        self.fields['byline'].widget.attrs['class'] = 'input is-medium'
        self.fields['featured_image'].widget.attrs['class'] = 'file-input'
        self.fields['tags'].widget.attrs['class'] = 'input is-large'

