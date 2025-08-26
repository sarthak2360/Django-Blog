from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    # categories = Category.objects.all() #this work is done by the context processor that we have added for all the web pages 
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    context ={
        # 'categories' : categories, #this work is done by the context processor that we have added for all the web pages 
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(request,'home.html',context)