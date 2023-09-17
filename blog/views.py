from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post

def blog_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context)

def post_detail(request, year, month, day, post):
    post_obj = get_object_or_404(Post,
                                 status=Post.Status.PUBLISHED,
                                 slug=post,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    context = {
        'post': post_obj,
    }
    return render(request, 'blog/post_detail.html', context)
