from django.shortcuts import render,  Http404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from .models import Posts, Like, Comments

# Create your views here.
posts = [
    {'id': 1, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news53.jpg', 'category': 'FOOTBALL'},
    {'id': 2, 'title': 'Erik Jones Has Day He Won’t Soon Forget As Denny Backup At Bristol','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news54.jpg', 'category': 'DIVING'}, 
    {'id': 3, 'title': 'A Taste Of What We Like This Week At CookA Like This Current Week','date': 'May 27, 2017', 'description': 'Separatede in the coast of the a ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news55.jpg', 'category': 'CYCLING'},
    {'id': 4, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news56.jpg', 'category': 'FOOTBALL'}, 
    {'id': 5, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news53.jpg', 'category': 'FOOTBALL'},
    {'id': 6, 'title': 'Erik Jones Has Day He Won’t Soon Forget As Denny Backup At Bristol','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news54.jpg', 'category': 'DIVING'}, 
    {'id': 7, 'title': 'A Taste Of What We Like This Week At CookA Like This Current Week','date': 'May 27, 2017', 'description': 'Separatede in the coast of the a ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news55.jpg', 'category': 'CYCLING'},
    {'id': 8, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news56.jpg', 'category': 'FOOTBALL'},
    ]

def home(request):
    contact_list = Posts.objects.all().order_by('-created')
    # like = Like.objects.filter(post=post).count()
    # comments = Comments.filter(post=post).count()
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
