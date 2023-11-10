from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm

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

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        # Form was submmited
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, 
                      message, 
                      'lord.smrha@gmail.com',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post': post,
        'form': form,
        'sent': sent
    }
    return render(request, 'blog/post/share.html', context)