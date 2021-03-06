from django.contrib import admin
from .models import Article, Category


'''
make model Admin :
    using namespace message_user to send a message top of admin view
    short_description to desribe 

    add to actions name of function to run 
'''

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    modeladmin.message_user(request,'successfuly make published')
make_published.short_description = "Mark selected stories as published"

def make_draft(modeladmin, request, queryset):
         queryset.update(status='d')
         modeladmin.message_user(request,'successfuly make draft')

make_draft.short_description = "Mark selected stories as draft"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'parent','slug' , 'position')
    list_filter =(['status'])
    search_fields = ('title' , 'description', 'slug')


admin.site.register(Category , CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'status' , 'slug','category_to_str')
    list_filter =('publish' , 'status' , 'slug')
    search_fields = ('title', 'description')
    actions = [make_published , make_draft]
    def category_to_str(self,obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.shor_description = 'categ'


admin.site.register(Article , ArticleAdmin)

