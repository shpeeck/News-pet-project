from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from news.views import Like, Comments, Posts


User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'get_likes')
    search_fields = ('first_name', 'last_name')
    list_filter = []
    fieldsets = (
        ('Информация о пользователе', {'fields': ('first_name', 'last_name', 'get_likes')}),
        ('Коментарии', {
            'fields': ('get_comments',)}),
        ('Заблокировать пользователя', {
            'fields': ('user_active',)}),
            )
    readonly_fields = ('first_name', 'last_name', 'get_likes', 'get_comments',)
        
    def get_likes(self, obj):
        user_likes = Like.objects.filter(author=obj).count()
        if user_likes:
            return user_likes
        else:
            return '-'

    def get_comments(self, obj):
        from django.utils.html import format_html
        user_comments = Comments.objects.filter(author=obj)
        if user_comments:
            code = '<table><tbody><tr><th>Пост</th><th>Коментарий</th></tr>'
            for i in user_comments:
                code +=f'<tr><td>{i.post.title}</td><td>{i.body}</td></tr>'
            return format_html(code + '</tbody></table>')
        else:
            return '-'

    
    get_likes.short_description = 'Кол-во лайков'
    get_comments.short_description = 'Коментарии'
