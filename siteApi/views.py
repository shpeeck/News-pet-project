from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from news.models import Posts, Like, Comments, Heading
from accounts.models import User
from .serializers import PostsSerializer, LikesSerializer, CommentsSerializer,  ProfileSerializer, CatSerializer, TopSerializer, GetProfileSerializer, FoolPostSerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

from datetime import datetime
import dateutil.relativedelta as relativedelta


class PostsApiView(ModelViewSet, LimitOffsetPagination):
    queryset = Posts.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories']
    search_fields = ['title']
    serializer_class = PostsSerializer
    http_method_names = ['get', 'head']


@api_view(http_method_names=['GET'])
def post(request, post_id):
    post = Posts.objects.get(id=post_id)
    all_likes = post.post_likes.count()
    comments = post.post_comments.all()
    all_comments = comments.count()
    comments_list = []
    for i in comments:
        comment = {
            'author': i.author.first_name, 
            'body': i.body,
            'created': i.created 
        }
        comments_list.append(comment)
    data = {'title': post.title, 'body': post.body, 'image': post.image, 'comments': comments_list, 'likes': all_likes, 'all_comments': all_comments}
    print('data', data)
    serializer = FoolPostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(http_method_names=['GET'])
@permission_classes((IsAuthenticated, ))
def get_user(request):
    return_dict = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email
        }
    serializer = GetProfileSerializer(data=return_dict)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def put_user(request):
    try:
        pk = request.user.id
    except:
        return Response({"error": "Method PUT not allowed"})
        pk = None
    try:
        instance = User.objects.get(id=pk)
    except:
        return Response({"error": "Object does not exists"})
    serializer = ProfileSerializer(data=request.data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def patch_user(request):
    try:
        pk = request.user.id
    except:
        return Response({"error": "Method PUT not allowed"})
        pk = None
    try:
        instance = User.objects.get(id=pk)
    except:
        return Response({"error": "Object does not exists"})
    serializer = ProfileSerializer(data=request.data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def like(request, post_id):
    post = Posts.objects.get(id=post_id)
    like = Like.objects.filter(post=post_id)
    user = request.user.id
    if len(like)>0:
        for i in like:
            if i.author.id==user:
                like = Like.objects.filter(author=user)
                like.delete()
            else:
                likes = Like.objects.create(post = post, author = request.user, like = True)
                return Response(data="like add", status=HTTP_201_CREATED)
    else:
        likes = Like.objects.create(post = post, author = request.user, like = True)
        return Response(data="like add", status=HTTP_201_CREATED)
    return Response(data="Delete", status=HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def post_comment(request, post_id):
    post = Posts.objects.get(id=post_id)
    user = request.user.id
    data = {'post': post_id, 'author': user, 'body': request.body.decode('utf-8'), 'created': datetime.now().date()}
    serializer = CommentsSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=HTTP_201_CREATED, data=serializer.data)


class CatApiView(ModelViewSet):
    queryset = Heading.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_names']
    serializer_class = CatSerializer
    http_method_names = ['get', 'head']
    pagination_class = None


@api_view(['GET'])
def top_news(request):
    three_days = datetime.now().today() - relativedelta.relativedelta(days=3)
    posts = Posts.objects.filter(created__gte=three_days)
    top = []
    for i in posts:
        like = Like.objects.filter(post=i.id).count()
        comments = Comments.objects.filter(post=i.id).count()
        if like >= 10 and comments >= 10:
            post = {
                'id': i.id,
                'title': i.title,
                'body': i.body,
                'like': like,
                'comments': comments
            }
            serializer = TopSerializer(data=post)
            serializer.is_valid(raise_exception=True)
            top.append(serializer.data)
    return Response(status=HTTP_200_OK, data=top)