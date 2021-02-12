from django.shortcuts import render

# Create your views here.
from AppBlog.models import Post, Categoria

def Blog(request):
    posts=Post.objects.all()
    return render(request,"AppBlog/blog.html",{"posts":posts})

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"AppBlog/categoria.html",{"categoria":categoria, "posts":posts})
