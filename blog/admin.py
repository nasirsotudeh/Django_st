from django.contrib import admin
from .models import Article , Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'slug' , 'position')
    list_filter =(['status'])
    search_fields = ('title' , 'description', 'slug')


admin.site.register(Category , CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'slug','category_to_str')
    list_filter =('publish' , 'status' , 'slug')
    search_fields = ('title', 'description')
    
    def category_to_str(self,obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.shor_description = 'categ'


admin.site.register(Article , ArticleAdmin)
