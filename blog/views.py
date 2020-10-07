from django.shortcuts import render , get_object_or_404 , get_list_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView , DetailView

class Articlelist(ListView):
    # use class view 
    # models = Article
    template_name="blog/main.html"
    queryset = Article.objects.published()
    paginate_by = 3

class ArticleDetail(DetailView):
    template_name ="blog/singel.html"     
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
class CategoryList(ListView):
    paginage_by = 7
    template_name = "blog/category.html"
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')     
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category 
        return context

    

# Create your views here.
# def home(request):
         
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 8)

#     page = request.GET.get('page')
#     articles = paginator.get_page(page)

#     context = {
#         'articles': articles
#     }
#     return render(request, 'blog/main.html', context)

# ########################
# def detail_article(request , slug):
#     context = {
#         'article' : get_object_or_404(Article , slug = slug)
#     }
#     return render(request ,'blog/singel.html', context)
# ########################
# def category(request, slug , page = 1):
#     category = get_object_or_404(Category, slug=slug)
#     articles_list = category.articles.published()
#     context = {
#         'category':category
#     }
#     return render(request, 'blog/category.html', context)


