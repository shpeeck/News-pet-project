from django.db import models
from accounts.models import User


class Posts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    categories = models.ForeignKey('Heading', on_delete=models.CASCADE, related_name='category', blank=True)
    image = models.ImageField(upload_to='static/images/', default='static/images/none.jpg', blank=True, null=True)
    alt_image = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name =  'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return 'Comment by {} on {}'.format(self.author, self.body)

    class Meta():
        verbose_name =  'Коментарий'
        verbose_name_plural = 'Коментарии'

class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField('like', default=False)


class Heading(models.Model):
    category_names = models.CharField(max_length=150)

    def __str__(self):
            return self.category_names

    class Meta():
        verbose_name =  'Рубрика'
        verbose_name_plural = 'Рубрики'