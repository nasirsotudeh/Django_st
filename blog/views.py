from django.shortcuts import render , get_object_or_404 , get_list_or_404
from .models import Article, Category
from django.core.paginator import Paginator


# Create your views here.
def home(request):
         
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 8)

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles
    }
    return render(request, 'blog/main.html', context)
    
########################
def detail_article(request , slug):
    context = {
        'article' : get_object_or_404(Article , slug = slug)
    }
    return render(request ,'blog/singel.html', context)
########################
def category(request, slug , page = 1):
    category = get_object_or_404(Category, slug=slug)
    articles_list = category.articles.published()
    context = {
        'category':category
    }
    return render(request, 'blog/category.html', context)


