from django.contrib import admin
from blog.models import Post ,PostImage ,Category ,Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostImage)
admin.site.register(Tag)

# Register your models here.
