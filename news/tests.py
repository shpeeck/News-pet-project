from django.test import TestCase
from django.urls import reverse

from news.models import Posts, Heading

class PostsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 10
        cat = Heading.objects.create(category_names='Cat')
        for post_num in range(number_of_posts):
            Posts.objects.create(title='Test %s' % post_num, body = 'Test %s' % post_num, categories=cat, image=None, alt_image='test')

    def test_view_url_one_post(self):
        resp = self.client.get('/one_post/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_category(self):
        resp = self.client.get('/category/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_redirrect(self):
        resp = self.client.get('/category/1')
        self.assertEqual(resp.status_code, 301)

    def test_search(self):
        resp = self.client.get('/?search=а/')
        self.assertEqual(resp.status_code, 200)


