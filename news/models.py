from django.db import models
from accounts.models import User


class Posts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    categories = models.ForeignKey('Heading', on_delete=models.CASCADE, related_name='category', blank=True)
    # category = models.CharField(
    #     choices=(
    #         ('политика', 'политика'), 
    #         ('бизнес', 'бизнес'), 
    #         ('спорт', 'спорт'),
    #         ('мода', 'мода'),
    #         ('путешествия', 'путешествия')
    #     ), 
    #     max_length=20, 
    #     default='политика')
    image = models.ImageField(upload_to='static/images/', default='static/images/none.jpg', blank=True, null=True)
    alt_image = models.CharField(max_length=50)
    likes = models.ForeignKey('Like', null=True, on_delete=models.CASCADE, related_name='likes', blank=True)
    comments_post = models.ForeignKey('Comments', null=True, related_name='comments_post', on_delete = models.DO_NOTHING, blank=True)


    def __str__(self):
        return f"{self.title}"

    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name =  'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True)
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
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField('like', default=False)


class Heading(models.Model):
    category_names = models.CharField(max_length=150)

    def __str__(self):
            return self.category_names

    class Meta():
        verbose_name =  'Рубрика'
        verbose_name_plural = 'Рубрики'