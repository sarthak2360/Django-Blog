from django.contrib import admin
from .models import Category
from .models import Blog

#this claas is added in admin.py top generate our slug automatically as we write our title of blog
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug' : ('title',)} # this prepopulated is a defined feature in django for slug 
    list_display = ('title' , 'category' , 'author' ,'status' ,  'is_featured')
    search_fields = ('id','title', 'category__category_name','status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)