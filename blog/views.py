
from django.views import generic
from .models import Post, Category
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostListNews(generic.ListView):
    queryset = Post.objects.filter(category_id=1)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostListFeira(generic.ListView):
    queryset = Post.objects.filter(category_id=2)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostListFinanceiro(generic.ListView):
    queryset = Post.objects.filter(category_id=3)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostListTransparencia(generic.ListView):
    queryset = Post.objects.filter(category_id=4)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostListEventos(generic.ListView):
    queryset = Post.objects.filter(category_id=5)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostListInformativos(generic.ListView):
    queryset = Post.objects.filter(category_id=6)
    if queryset:
        template_name = 'blog.html'
    else:
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        template_name = 'blog.html'


class PostIndex(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "landing.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# def postDetail(request):
#     detail_list = Post.objects.filter(status=1).order_by('-created_on')
#     context = {'detail_list': detail_list}
#     return render(request, 'post_detail.html', context)
'''
def landing(request):
    return render(request, 'landing.html')'''


def sobre(request):
    return render(request, 'sobre.html')


def land_page(request):
    return render(request, 'base.html')


def regimentos(request):
    return render(request, 'regimentos.html')


def estatuto(request):
    return render(request, 'estatuto.html')


def contato(request):
    return render(request, 'contact.html')


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})
