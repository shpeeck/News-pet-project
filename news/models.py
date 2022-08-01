from django.db import models
from accounts.models import User


# Create your models here.
class Posts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.CharField(
        choices=(
            ('политика', 'политика'), 
            ('бизнес', 'бизнес'), 
            ('спорт', 'спорт'),
            ('мода', 'мода'),
            ('путешествия', 'путешествия')
        ), 
        max_length=20, 
        default='политика')
    image = models.ImageField(upload_to='static/images/', default='static/images/none.jpg', blank=True, null=True)
    alt_image = models.CharField(max_length=50)
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # likes = models.ManyToManyField(User, related_name="liked_posts")

    # @staticmethod
    # def create_books():
    #     from .views import books
    #     for i in books:
    #         book = Books(title=i['title'], released_year=i['released_year'], description=i['description'], author_id=i['author_id'])
    #         book.save()

    def __str__(self):
        return f"{self.pk} {self.title} {self.image} {self.likes}"

    class Meta():
        verbose_name =  'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return 'Comment by {} on {}'.format(self.author, self.body)

    class Meta():
        verbose_name =  'Comment'
        verbose_name_plural = 'Comments'

class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)