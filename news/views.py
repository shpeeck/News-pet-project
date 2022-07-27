from django.shortcuts import render,  Http404
from django.http import HttpRequest, HttpResponse

# Create your views here.
posts = [
    {'id': 1, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news53.jpg', 'category': 'FOOTBALL'},
    {'id': 2, 'title': 'Erik Jones Has Day He Won’t Soon Forget As Denny Backup At Bristol','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news54.jpg', 'category': 'DIVING'}, 
    {'id': 3, 'title': 'A Taste Of What We Like This Week At CookA Like This Current Week','date': 'May 27, 2017', 'description': 'Separatede in the coast of the a ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news55.jpg', 'category': 'CYCLING'},
    {'id': 4, 'title': 'Football Meras On The Back SepatheyTG G6 Will Have Theytics.','date': 'May 27, 2017', 'description': 'Separated they right at the coast a large ocean. A small river named Duden flows by their place and ...', 'author_id': 'Jacob', 'foto': 'news56.jpg', 'category': 'FOOTBALL'}, 
    ]

def home(request):
    context = {'posts': posts}
    return render(request, 'news/index.html', context=context)

def foo(request):
    return render(request, 'news/index_test.html')

