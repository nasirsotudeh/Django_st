from django.contrib import admin
from .models import Article , Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'slug' , 'position')
    list_filter =(['status'])
    search_fields = ('title' , 'description', 'slug')


admin.site.register(Category , CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'slug')
    list_filter =('publish' , 'status' , 'slug')


admin.site.register(Article , ArticleAdmin)
