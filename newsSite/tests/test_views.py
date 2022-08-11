from django.test import TestCase
from django.urls import reverse

from news.models import Posts, Comments, Like, Heading
from accounts.models import User

# class YourTestClass(TestCase):

#     def setUp(self):
#         # Установки запускаются перед каждым тестом
#         pass

#     def tearDown(self):
#         # Очистка после каждого метода
#         pass

#     def test_something_that_will_pass(self):
#         self.assertFalse(False)

#     def test_something_that_will_fail(self):
#         self.assertTrue(False)


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_first_name_label(self):
        author=User.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'имя')

    def test_first_name_max_length(self):
        author=User.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,150)

    def test_object_mail(self):
        author=User.objects.get(id=1)
        expected_object_name = author.email
        self.assertEquals(expected_object_name,str(author))

    def test_is_user_active(self):
            author=User.objects.get(id=1)
            expected_object_name = author.user_active
            self.assertEquals(expected_object_name, True)

    # def test_is_user_verify(self):
    #     author=User.objects.get(id=1)
    #     expected_object_name = author.email_verify
    #     self.assertEquals(expected_object_name, True)


class HeadinglTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_first_name_label(self):
        author=User.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'имя')