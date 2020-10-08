from django.shortcuts import render , get_object_or_404 , get_list_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from . import models
from . import serializers
'''
Using Class view
    use namespace template_name to find HTML file and paginate_by for paginate
    in HTML file in Templates can use objects that made from ListVew in my class
    using namespace queryset to get all oblect
    in DetailView can write function and pass all kwargs and use custum kwargs
'''
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

'''
using Class view in serialiser
    using namespace queryset to get all oblect
    serialize = serializers.ArticleSerializer get field serializer
    serializer_class namespace create API veiw as serialisers.py
    use lookup_field = 'slug' to change pk that framework lock for to get kwargs from url 
'''
class ListArticle(APIView):
         def get(self,request ,format=None):
            cors = models.Article.objects.all()
            serialize = serializers.ArticleSerializer(cors, many=True)
            return Response(serialize.data)

         def post(self, request, format=None):
            serializer = serializers.ArticleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save
            return Response(serializer.data)

class ListCategory(generics.ListCreateAPIView):
         queryset = models.Category.objects.all()
         serializer_class = serializers.CategorySerializer
        
class ListCreateReview(generics.ListCreateAPIView):
         queryset = models.Article.objects.all()
         serializer_class = serializers.ArticleSerializer
         def get_queryset(self):
                  return self.queryset.filter(slug=self.kwargs.get('slug'))

class LiseUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
         lookup_field = 'slug'
         queryset = models.Article.objects.all()
         serializer_class = serializers.ArticleSerializer
         


