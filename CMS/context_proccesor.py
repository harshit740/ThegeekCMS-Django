from blog.models import Category


def getCategory(request):
    categry = Category.objects.all()
    for cat in categry:
        print(cat.slug)
    return {'categry':categry}