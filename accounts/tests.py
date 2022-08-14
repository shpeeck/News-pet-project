from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Doe', email='test@gmail.com', password='qw12we23er34')

    def test_first_name_label(self):
        author=User.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'имя')

    def test_last_name_label(self):
        author=User.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'фамилия')

    def test_email_label(self):
        author=User.objects.get(id=1)
        field_label = author._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'Почта')

    def test_first_name_max_length(self):
        author=User.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,150)

    def test_last_name_max_length(self):
        author=User.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length,150)

    def test_object_mail(self):
        author=User.objects.get(id=1)
        expected_object_name = author.email
        self.assertEquals(expected_object_name,str(author))

    def test_object_first_name(self):
        author=User.objects.get(id=1)
        expected_object_first_name = author.first_name
        self.assertEquals(expected_object_first_name, "John")

    def test_object_last_name(self):
        author=User.objects.get(id=1)
        expected_object_last_name = author.last_name
        self.assertEquals(expected_object_last_name, "Doe")

    def test_is_user_active(self):
            author=User.objects.get(id=1)
            expected_object_name = author.user_active
            self.assertEquals(expected_object_name, True)

    def test_user_is_active(self):
            author=User.objects.get(id=1)
            expected_object_name = author.is_active
            self.assertEquals(expected_object_name, True)