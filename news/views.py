from django.shortcuts import render,  Http404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from .models import Posts, Like, Comments

# Create your views here.
def home(request):
    contact_list = Posts.objects.all().order_by('-created')
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        contact_list = Posts.objects.filter(title__icontains=search)

    paginator = Paginator(contact_list, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'news/index.html', {'posts': contacts})


def post(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
        like = Like.objects.filter(post=post_id).count()
        comments = Comments.objects.filter(post=post_id)
        all_comments = comments.count()
        # autor = Autors.objects.get(pk=book.author_id)
        # comments = Comments.objects.filter(book_id=book_id).order_by('-created')
        # if request.method == "POST":
        #     form = CommentForm(request.POST)
        #     if form.is_valid():
        #         form.book = book_id
        #         new_form = form.save(commit=False)
        #         new_form.name = request.user
        #         new_form.book = book
        #         new_form.save()
        # return render(request, 'news/post.html', context={'book': book, 'autor': autor, 'comments': comments, 'post_form': CommentForm})
        return render(request, 'news/post.html',context={'post': post, 'like': like, 'comments': comments, 'all_comments': all_comments})

    except Posts.DoesNotExist: 
        raise Http404(f"Not found post_id {post_id}")
