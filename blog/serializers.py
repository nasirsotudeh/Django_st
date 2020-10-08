from . import models
from rest_framework import routers, serializers, viewsets





class ArticleSerializer(serializers.ModelSerializer):
     class Meta:
          lookup_field = 'slug' 
          extra_kwargs = {
               'email': {'write_only': True} ,
               'url': {'lookup_field': 'slug'}
          }
          fields = (
               'title',
               'slug',
               'describtion',
               'publish',
               'craeted',
          )
              
          model = models.Article

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          fields = (
               'parent',
               'title',
               'status'
          )
          model = models.Category

