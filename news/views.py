from django.shortcuts import render,  Http404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from .models import Posts, Like, Comments, Heading


def new_base(request, id):
    contact_list = Posts.objects.filter(categories=id).order_by('-created')
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        contact_list = Posts.objects.filter(title__icontains=search)

    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'news/category.html', {'posts': contacts})


def home(request):
    contact_list = Posts.objects.all().order_by('-created')
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        contact_list = Posts.objects.filter(title__icontains=search)

    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'news/index.html', {'posts': contacts})


def one_post(request, post_id):
    try:
        one_post = Posts.objects.get(pk=post_id)
        like = Like.objects.filter(post=post_id).count()
        comments = Comments.objects.filter(post=post_id)
        all_comments = comments.count()
        context={
            'one_post': one_post, 
            'like': like, 
            'comments': comments, 
            'all_comments': all_comments
            }
        return render(request, 'news/post.html', context=context)

    except Posts.DoesNotExist: 
        raise Http404(f"Not found post_id {post_id}")
