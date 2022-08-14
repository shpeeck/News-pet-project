from django.db import connection
from django.urls import include, path, reverse
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.test import Client 

from django.test import TestCase
from news.models import Posts, Comments, Like, Heading
from accounts.models import User


class  HeadingTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 5
        for post_num in range(number_of_posts):
            Heading.objects.create(category_names=f'Cat{post_num}')

    def test_get_categories(self):
        response = self.client.get('http://127.0.0.1:8000/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 5)
        self.assertEqual(Heading.objects.get(pk=1).category_names, 'Cat0')
        self.assertEqual(len(response.data), 5)

    def test_search_category(self):
        response = self.client.get('http://127.0.0.1:8000/api/categories/?search=Cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 5)
        self.assertEqual(len(response.data), 5)

        response = self.client.get('http://127.0.0.1:8000/api/categories/?search=cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 5)
        self.assertEqual(len(response.data), 5)


class  UserTests(APITestCase):

    @classmethod
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_is_user_create(self):
        self.assertEqual(User.objects.get(pk=1).email, 'test@gmail.com')

    def test_get_token(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        
    def test_get_user_data(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('http://127.0.0.1:8000/api/get/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'first_name': 'John', 'last_name': 'Doe', 'email': 'test@gmail.com'})

    def test_change_user_data(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.put('http://127.0.0.1:8000/api/put/profile', {'first_name': 'June'})
        self.assertEqual(response.status_code, 301)
        response = self.client.patch('http://127.0.0.1:8000/api/put/profile', {'first_name': 'June'})
        self.assertEqual(response.status_code, 301)


class PostsTests(APITestCase):
    
    @classmethod
    def setUp(self):
        number_of_posts = 13
        cat = Heading.objects.create(category_names='Cat')
        for post_num in range(number_of_posts):
            Posts.objects.create(title='Test %s' % post_num, body = 'Test %s' % post_num, categories=cat, image=None, alt_image='test')

    def test_is_posts_create(self):
        response = self.client.get(reverse('all_news'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Posts.objects.count(), 13)
        self.assertEqual(Posts.objects.get(pk=1).title, 'Test 0')

    def test_is_posts_pagination(self):
        response = self.client.get(reverse('all_news'))
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['next'], 'http://testserver/api/all-news/?limit=3&offset=3')
        next_page = response.data['next']
        response = self.client.get(next_page)
        self.assertEqual(response.status_code, 200)

    def test_posts_filter(self):
        response = self.client.get('http://127.0.0.1:8000/api/all-news/?search=Test 9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)


    def test_posts_search(self):
        response = self.client.get('http://127.0.0.1:8000/api/all-news/?category=Cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 13)


class OnePostTests(APITestCase):
    
    @classmethod
    def setUp(self):
        cat = Heading.objects.create(category_names='Cat')
        Posts.objects.create(title='Test', body = 'Test', categories=cat,  alt_image='test')

    def test_is_post_create(self):
        response = self.client.get('http://127.0.0.1:8000/api/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test')
        self.assertEqual(response.data['body'], 'Test')
        self.assertEqual(response.data['image'], '/static/images/none.jpg')
        self.assertEqual(response.data['likes'], 0)
        self.assertEqual(response.data['comments'], [])
        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(Posts.objects.get(pk=1).id, 1)


class LikeTests(APITestCase):
    
    @classmethod
    def setUp(self):
        cat = Heading.objects.create(category_names='Cat')
        Posts.objects.create(title='Test', body = 'Test', categories=cat,  alt_image='test')
        self.user = User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_like_create(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.put('http://127.0.0.1:8000/api/like/1/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.filter(post=1).count(), 1)

    def test_like_delete(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.put('http://127.0.0.1:8000/api/like/1/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.filter(post=1).count(), 1)
        response = self.client.put('http://127.0.0.1:8000/api/like/1/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.filter(post=1).count(), 0)


class CommentTests(APITestCase):
    
    @classmethod
    def setUp(self):
        cat = Heading.objects.create(category_names='Cat')
        Posts.objects.create(title='Test', body = 'Test', categories=cat,  alt_image='test')
        self.user = User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_like_create(self):
        token = Token.objects.get_or_create(user=self.user) 
        token = str(token[0])
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
        post = Posts.objects.get(pk=1)
        data = {'post': post, 'author': self.client, 'body': 'its a new comment'}
        response = self.client.post('http://127.0.0.1:8000/api/post_comment/1/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comments.objects.filter(post=1).count(), 1)
        response = self.client.post('http://127.0.0.1:8000/api/post_comment/1/', data, format='json')
        self.assertEqual(Comments.objects.filter(post=1).count(), 2)

class TopNewsTests(APITestCase):
    
    @classmethod
    def setUp(self):
        cat = Heading.objects.create(category_names='Cat')
        number_of_posts = 13
        for post_num in range(number_of_posts):
            Posts.objects.create(title='Test %s' % post_num, body = 'Test %s' % post_num, categories=cat, alt_image='test')
        

    def test_like_create(self):
        number_of_users = 11
        for user_num in range(number_of_users):
            user = User.objects.create(first_name=f'John{user_num}', last_name='Doe{user_num}', email=f'test{user_num}@gmail.com', password='qw12we23er34{user_num}')
            token = Token.objects.get_or_create(user=user) 
            token = str(token[0])
            self.client = Client(HTTP_AUTHORIZATION='Token ' + token)
            response = self.client.put('http://127.0.0.1:8000/api/like/1/')
            self.assertEqual(response.status_code, 201)
            post = Posts.objects.get(pk=1)
            data = {'post': post, 'author': self.client, 'body': 'its a new comment'}
            response = self.client.post('http://127.0.0.1:8000/api/post_comment/1/', data, format='json')
            self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.filter(post=1).count(), 11)
        self.assertEqual(Comments.objects.filter(post=1).count(), 11)
        response = self.client.get(reverse('top_news'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

