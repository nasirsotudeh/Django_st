from django.shortcuts import render , get_object_or_404 , get_list_or_404

from .models import Article , Category

# Create your views here.


def home(request):

    context = {
        'articles': Article.objects.filter(),
        'category' : Category.objects.filter(),
    }
    return render(request ,'blog/main.html', context)
########################

def detail_article(request , slug):
    context = {
        'article' : get_object_or_404(Article , slug = slug)
    }
    return render(request ,'blog/singel.html', context)

########################

def category(request, slug):
         
    context = {
        'category' : get_object_or_404(Category , slug= slug)
    }
    return render(request, 'blog/category.html', context)


