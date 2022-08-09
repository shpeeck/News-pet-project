from django.db import connection
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

from django.test import TestCase
from news.models import Posts, Comments, Like, Heading
from accounts.models import User


class  HeadingTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 1
        for post_num in range(number_of_posts):
            Heading.objects.create(category_names='Cat')


    def test_positive(self):
        # response = self.client.get(reverse('cat'))
        response = self.client.get('http://127.0.0.1:8000/api/categories/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 1)
        self.assertEqual(Heading.objects.get().category_names, 'Cat')
        self.assertEqual(len(response.data), 1)

        response = self.client.get('http://127.0.0.1:8000/api/categories/?search=Cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 1)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{"category_names": "Cat"}])

        response = self.client.get('http://127.0.0.1:8000/api/categories/?search=cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Heading.objects.count(), 1)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{"category_names": "Cat"}])


        





