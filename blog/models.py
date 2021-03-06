from django.db import models
from django.utils import timezone


# my manager for manage filter
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
        
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# category
class Category(models.Model):
    parent = models.ForeignKey('self',default =None , null=True, blank=True, on_delete=models.SET_NULL, related_name ='childeren', verbose_name='subText')
    title = models.CharField(max_length=200 , verbose_name="Category")
    slug = models.SlugField(max_length=100 , unique=True, verbose_name="slug")
    status = models.BooleanField(default = True , verbose_name ="show?")
    position = models.IntegerField(verbose_name="position")
    class Meta:
        ordering = ['parent__id','position']
    def __str__(self):
        return self.title
    objects = CategoryManager()


# Article
class Article(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 100 , unique = True)
    describtion = models.TextField()
    category = models.ManyToManyField(Category , verbose_name = 'categorys', related_name="articles")
    thumbnail = models.ImageField(upload_to='media')
    publish = models.DateTimeField(default=timezone.now)
    craeted = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    STATUS_CHOICES =(
        ('d' , 'Draft'),
        ('p' , 'Publish')
    )

    status = models.CharField(max_length = 1 , choices =STATUS_CHOICES )
    def __str__(self):
        return self.title
    def category_published(self):
        return self.category.filter(status=True)
    objects = ArticleManager()
  




    # class Meta :
             
    #     ordering = ['published']
 
    # def __str__(self):
    #          return self.title
    
    # objects = ArticleManager()


